import yaml
import sys

import challonge
import requests.exceptions

from . import setup

URL = "https://api.challonge.com/v1/tournaments"







def setupChallonge():
    """
    Prepares Challonge for usage.
    
    Should be called before any other actions with Challonge library are taken
    """    
    print("setuping!")
    #TODO: loads credentials from an external file, this should, in future, be done through the environment
    
    credentials = setup.getLogin()

    if credentials["username"] == None or credentials["APIKey"] == None:
        raise ValueError("Username or API key are not filled in!")
    
    challonge.set_credentials(credentials["username"], credentials["APIKey"])


def formateParams(params, formatingDict):
    """
    given a dict of unformated parameters, it will format each of the values (i.e. call .format on them)
    """
    formatedParams = {}
    for key in params:
        if type(params[key]) != type(""):
            formatedParams[key] = params[key]
            continue
        formatedParams[key] = params[key].format(**formatingDict)
    return formatedParams
    
def safeRequest(request):
    """
    makes a reqest while handling all exceptions
    
    if a request fails, ConnectionError is raised with appropriate error message
    request: () => void
    """
    
    try:
        return request()
    except requests.exceptions.RequestException as e:
        with open("log", "w") as log:
            print(e, file=log)
        
        #401 == unauthorized    
        if e.response.status_code == 401:
            raise ConnectionError("Wrong username and password!")
        
        #404 == page not foun
        if e.response.status_code == 404:
            raise ConnectionError("Can't find required page! If this shouldn't happen, please check you are using current version of this software. If problem persists, contact the author.")
            
        raise ConnectionError(*e.args)
         
    except requests.exceptions.Timeout:
        raise ConnectionError("Can't connect to Challonge. Check it's up and try it again!", file=sys.stderr)
    
    except challonge.api.ChallongeException as e:
        raise ConnectionError(*e.args)
        
    
def createTournament(**params):
    """
    will create a new tournament with given parameters
    
    name is required!
    
    """
    myParams = {"url": None}
    myParams.update(params)
    print(myParams)
    a = safeRequest(lambda: challonge.tournaments.create(**myParams))
    
    print("tournament created")
    
    with open("log", "w") as log:
        print(a, file=log)
        
    return a["id"]


def deleteTournament(id):
    """
    will delete tournament with given id
    """
    safeRequest(lambda: challonge.tournaments.destroy(id))

def readTournament(id):
    """
    will delete tournament with given id
    """
    print(safeRequest(lambda: challonge.tournaments.show(id)), file=sys.stderr)
    

def main(config, deleteAfterwards, formatingDict):
    """
    config is the yaml read from the config file
    
    deleteAfterwards is a switch that tells us if we should delete the tournament before terminating
    
    keywords are the words that will be used in the template
    """

    setupChallonge()
    
    try:
        tournamentId = createTournament(**formateParams(config, formatingDict))
    except ConnectionError as e:
        print()  
        print("\n".join(e.args))
        return
        
        
    if deleteAfterwards:
        while True:
            answer = input("do you want to delete the tournament? [Y/N]")
            if len(answer) == 0:
                continue
                
            if answer[0].lower() == "n":
                break
            if answer[0].lower() == "y":
                deleteTournament(tournamentId)
                break
            