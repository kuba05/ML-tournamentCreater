import yaml

def isLoggedIn():
    """
    checks if user have filled credentials
    """
    login = getLogin()
    return login["username"] != None and ["password"] != None
    


def getLogin():
    """
    return current credentials
    """
                
    try:
        with open("config/credentials.yaml") as credentials:
            loaded = yaml.safe_load(credentials)
            return {"username": loaded["username"], "password": loaded["password"]}
        
    except Exception:
        return {"username": None, "APIKey": None, "password": None}



def setupAuthentication():
    """
    checks user is loged in as he wants to be
    """
    
    if isLoggedIn():
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
    print("Please log in!", flush=True)
    
    username = input("Username: ").strip()
    
    password = input("Password: ").strip()
    
    with open("config/credentials.yaml", "w") as credentials:
        credentials.write(yaml.dump({"username": username, "password": password}))
