from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


from core.setup import isLoggedIn, getLogin


username = None
password = None
ROOT = "https://challonge.com"    



def setup():
    """
    creates selenium driver and returns it
    """
    global username, password
    
    # get credentials
    
    if not isLoggedIn():
        raise ValueError("Username or password are not filled in!")
     
    credentials = getLogin()

    username = credentials["username"]
    password = credentials["password"]
    
    
    driver = webdriver.Chrome(executable_path = "core/sel/chromedriver.exe")
    
    return driver



def login(driver):
    #loads the page
    driver.get(ROOT + "/user_session/new?continue=%2F")
    
    #finds the login form
    loginForm = driver.find_element(By.ID, "new_user_session")
    
    #fills the form in
    loginForm.find_element(By.ID, "user_session_username_or_email").send_keys(username)
    loginForm.find_element(By.ID, "user_session_password").send_keys(password)
    
    #sumbits the form
    loginForm.find_element(By.XPATH, '//input[@type="submit"]').click()



def findTournament(driver, id):
    driver.get(ROOT + f"/{id}")

    
def addjustSettings(driver, tournamentURL, settings):
    
    # goes to the settings page of tournament
    try:
        # make the loading faster
        driver.set_page_load_timeout(5)
        driver.get(ROOT + f"/{tournamentURL}/settings")
    except Exception:
        pass
        
    # return to default
    driver.set_page_load_timeout(300)    
    
    # finds the form
    form = driver.find_element(By.ID, "tournament_form")
    
    # set the settings
    for setting in settings:
        
        try:
        
            element = form.find_element(By.XPATH, f"//*[@name='{setting}']")
            
            # if the value is Bool, the target element is a switch
            if isinstance(settings[setting], bool):
                
                #the current value is different from the expected one
                if element.is_selected() != settings[setting]:
                
                    #the element is often unclickable, hence we have to use js
                    driver.execute_script("arguments[0].click()", element)
                    
                    with open("log", "a") as log:
                        print(f"{setting} changed to {settings[setting]}", file=log)
            
            if isinstance(settings[setting], str) or isinstance(settings[setting], int):
                if element.get_attribute("value") != settings[setting]:
                    driver.execute_script("arguments[0].value = arguments[1]", element, settings[setting])
                    
                    
        except Exception as e:
            with open("log", "a") as log:
                print(e, file=log)
    
    # sumbit the form
    btn = driver.find_element(By.XPATH, "//input[@value='Save Changes']")
    input("Please check the settings and e.g. set time! Then continue by pressing enter in this window.")
    driver.execute_script("arguments[0].click()", btn)

def prepare():    
    driver = setup()
    login(driver)
    return driver
    
def stopSelenium(driver):
    driver.quit()
    
    
if __name__ == "__main__":
    driver = prepare()
    id = input("please enter tournament id:")
    findTournament(driver, id)
    input()
    driver.quit()
