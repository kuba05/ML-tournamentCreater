import yaml
import sys

import challonge
import requests.exceptions

from . import setup








def _setupChallonge():
    """
    Prepares Challonge for usage.
    
    Should be called before any other actions with Challonge library are taken
    """    
    if not setup.isLoggedIn():
        raise ValueError("Username or API key are not filled in!")
        
    credentials = setup.getLogin()

    challonge.set_credentials(credentials["username"], credentials["APIKey"])

    
    
def _safeRequest(request):
    """
    makes a reqest while handling all exceptions
    
    if a request fails, ConnectionError is raised with appropriate error message
    request: () => void
    """
    
    try:
        return request()
    except requests.exceptions.RequestException as e:
        with open("log", "a") as log:
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
        
    
    
def _createTournament(**params):
    """
    will create a new tournament with given parameters
    
    name is required!
    
    """
    myParams = {"url": None}
    myParams.update(params)
    
    a = _safeRequest(lambda: challonge.tournaments.create(**myParams))
    
    with open("log", "a") as log:
        print(a, file=log)
        
    return a["url"]



def _deleteTournament(id):
    """
    will delete tournament with given id
    """
    _safeRequest(lambda: challonge.tournaments.destroy(id))



def _readTournament(id):
    """
    will delete tournament with given id
    """
    print(_safeRequest(lambda: challonge.tournaments.show(id)), file=sys.stderr)


    
def _preproccessConfig(config):
    """
    there are many fields in the config we do not care about in this part
    and the rest needs to be in different format for challonge to work
    """
    parsedConfig = {}
    for key in config:
        if "[" not in key:
            pass
        splited = key[:-1].split("[", 1)
        if splited[0] != "tournament":
            continue
        parsedConfig[splited[1]] = config[key]
    
    return parsedConfig
        
        
        
def createTournament(config):
    """
    config is dictionary of options that will be passed to the API
    """
    _setupChallonge()
    parsedConfig = _preproccessConfig(config)
    try:
        tournamentURL = _createTournament(**parsedConfig)
    except ConnectionError as e:
        print()  
        print("\n".join(e.args))
        return config["tournament[url]"]
    
    return tournamentURL
        
        
        
def deleteTournament(tournamentId):
    """
    ask user if he really wishes to delete tournament and if yes delete it
    """ 
    while True:
        answer = input("do you want to delete the tournament? [Y/N]")
        if len(answer) == 0:
            continue
            
        if answer[0].lower() == "n":
            break
        if answer[0].lower() == "y":
            _deleteTournament(tournamentId)
            break
        
