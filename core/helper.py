import sys

from datetime import datetime

types = {
    "bool": bool,
    "str": str,
    "int": int,
    "float": float,
    "date": datetime.fromisoformat
    #"date": lambda date: datetime.strptime(date, "%y %m %d %H")
}

def formateToType(text, type, paramName):
    if type in types:
        try:
            return types[type](text)
        except ValueError:
            print(f"{paramName} was not inputed correctly, defaulting to None.", file=sys.stderr)
            return None
            
    raise ValueError("{paramName} has an invalid type \"{type}\"!".format())

def loadFromEnviroment(params):
    """
    params: {
            [name: str]: type: str
        }
    """
    return {}
    
def loadFromUser(params):
    """
    params: {
            [name: str]: [text: str, type: str]
        }
    """
    output = {}
    for param in params:
        output[param] = formateToType(input(params[param][0]), params[param][1], param)
    
    return output
        