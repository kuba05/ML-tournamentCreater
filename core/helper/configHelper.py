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
            print(f"{paramName} was not inputed correctly, defaulting to None.", file=sys.stderr, flush=True)
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
    
        
def formateConfig(config, parameters):
    """
    given parameters, it will call .format() on all string values in config
    """
    
    # let's get dirty!
    locals().update(parameters)
    
    formatedConfig = {}
    
    for key in config:
        # if object is directory, we should format all its elements as well
        if type(config[key]) == type({1:1}):
            formatedConfig[key] = formateConfig(config[key], parameters)
            continue
        
        # it only makes sense to format strings
        if type(config[key]) != type(""):    
            formatedConfig[key] = config[key]
            continue
        
        # we need to use f string, as we need to allow for complicated expresions
        # see https://stackoverflow.com/questions/44757222/transform-string-to-f-string 
        formatedConfig[key] = eval(f"f{repr(config[key])}")
    
    return formatedConfig
        

def loadParamsFromConfigAndFormateConfig(config):
    if config["parameters"] == None:
        return config
        
    params = config["parameters"]
    params = dict(**loadFromEnviroment(params["env"]), **loadFromUser(params["user"]))
  
    # formate the config
    formatedConfig = formateConfig(
        # pass the whole config except for "parameters"
        {i: config[i] for i in config if i != "parameters"}
        , params
    )
    
    return formatedConfig
