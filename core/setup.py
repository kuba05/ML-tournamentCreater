import yaml

def isLogedIn():
    """
    checks if user have filled credentials
    """
    try:
        with open("config/credentials.yaml") as credentials:
            loaded = yaml.safe_load(credentials.read())
            return "APIKey" in loaded and loaded["APIKey"] != None and "username" in loaded and loaded["username"] != None
    except FileNotFoundError:
        return False

def getLogin():
    """
    return current credentials
    """
                
    try:
        with open("config/credentials.yaml") as credentials:
            loaded = yaml.safe_load(credentials.read())
            return loaded
    except Exception:
        return {"username":"", "APIKey": None}

def setup():
    """
    checks user is loged in as he wants to be
    """
    
    if isLogedIn():
        username = getLogin()["username"]
        while True:
            answer = input(f"Do you want to continue as {username}? [Y/N]")
            
            if answer[0].lower() == "y":
                return
            
            if answer[0].lower() == "n":
                break
    
    login()

def login():
    """
    makes user fill in credentials
    """
    print("Please log in!")
    
    username = input("Username: ").strip()
    
    APIKey = input("API key: ").strip()
    
    with open("config/credentials.yaml", "w") as credentials:
        credentials.write(yaml.dump({"username": username, "APIKey": APIKey}))