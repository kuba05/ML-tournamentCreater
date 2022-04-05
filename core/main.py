import yaml
import challonge
import sys

URL = "https://api.challonge.com/v1/tournaments"







def setup():
    """
    Prepares Challonge for usage.
    
    Should be called before any other actions with Challonge library are taken
    """    
    print("setuping!")
    #TODO: loads credentials from an external file, this should, in future, be done through the environment
    
    with open("config/credentials.yaml") as credentialsFile:
        credentials = yaml.safe_load(credentialsFile.read())

    if "username" not in credentials or "APIKey" not in credentials:
        raise ValueError("both username and password shall be provided in the credentails.yaml file!")
    if credentials["username"] == None or credentials["APIKey"] == None:
        raise ValueError("Please make sure to fill in real values in the credentials config!")
    
    challonge.set_credentials(credentials["username"], credentials["APIKey"])


def formateParams(params, formatingDict):
    """
    given a dict of unformated parameters, it will format each of the values (i.e. call .format on them)
    """
    formatedParams = {}
    for key in params:
        formatedParams[key] = str(params[key]).format(**formatingDict)
    return formatedParams
    
    
def createTournament(**params):
    """
    will create a new tournament with given parameters
    
    name is required!
    
    """
    myParams = {"url": None}
    myParams.update(params)
    
    a = challonge.tournaments.create(**myParams)
    
    with open("../log", "w") as log:
        print(a, file=log)
        
    return a["id"]


def deleteTournament(id):
    """
    will delete tournament with given id
    """
    challonge.tournaments.destroy(id)


def main(config, deleteAfterwards, formatingDict):
    """
    config is the yaml read from the config file
    
    deleteAfterwards is a switch that tells us if we should delete the tournament before terminating
    
    keywords are the words that will be used in the template
    """

    setup()
    tournamentId = createTournament(**formateParams(config, formatingDict))
    
    if deleteAfterwards:
        while True:
            answer = input("do you want to delete the tournament? [Y/N]")
            if answer[0].lower() == "n":
                break
            if answer[0].lower() == "y":
                deleteTournament(tournamentId)
                break
            