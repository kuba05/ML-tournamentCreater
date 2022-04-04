import yaml
import challonge
import sys 

URL = "https://api.challonge.com/v1/tournaments"






def setup():
    """
    Prepares Challonge for usage.
    
    Should be called before any other actions with Challonge library are taken
    """    
    
    #TODO: loads credentials from an external file, this should, in future, be done through the environment
    
    with open("../config/credentials.yaml") as credentialsFile:
        credentials = yaml.safe_load(credentialsFile.read())

    if "username" not in credentials or "password" not in credentials:
        raise ValueError("both username and password shall be provided in the credentails.yaml file!")
    if credentials["username"] == None or credentials["password"] == None:
        raise ValueError("Please make sure to fill in real values in the credentials config!")
    
    challonge.set_credentials(credentials["username"], credentials["password"])


def formateParams(**params):
    """
    given a dict of unformated parameters, it will format each of the values (i.e. call .format on them)
    """
    formatedParams = {}
    for key in params:
        formatedParams[key] = params[key].format()
        
    return formatedParams
    
    
def createTournament(**params):
    """
    will create a new tournament with given parameters
    
    name is required!
    
    """
    
    myParams = {"url": None}
    myParams.update(params)
    print(myParams)
    a = challonge.tournaments.create(**myParams)
    print(a["id"])
    print(a, file=sys.stderr)

def deleteTournament(id):
    """
    will delete tournament with given id
    """
    challonge.tournaments.destroy(id)




mode = sys.argv[1]
setup()
print(sys.argv)
if mode == "c":
    
    with open("../config/config.yaml") as configFile:
        config = yaml.safe_load(configFile.read())
    
    createTournament(**config)

if mode == "d":
    deleteTournament(sys.argv(2))