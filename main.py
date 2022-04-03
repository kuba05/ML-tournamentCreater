import yaml
import challonge
import sys 

URL = "https://api.challonge.com/v1/tournaments"

user = "gavlna"

with open("password.txt") as passwordFile:
    password = passwordFile.read()

print(password)

def setup(user, password):
    challonge.set_credentials(user, password)


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



setup(user, password)

mode = sys.argv[1]
print(sys.argv)
if mode == "c":
    
    if len(sys.argv) > 2: challonge.tournaments.destroy(sys.argv[2])
    
    config = open("./config.json")
    b = yaml.safe_load(config.read())
    config.close()
    
    createTournament(**b)

if mode == "d":
    pass