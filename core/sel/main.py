import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


from core.setup import isLoggedIn, getLogin

from config.config import ROOT

username = None
password = None



def setupSelenium():
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
    
    options = webdriver.ChromeOptions()
    
    try:
        driver = webdriver.Chrome(executable_path = "core/sel/chromedriver.exe", options = options)
    except Exception as e:
        raise e
    return driver



def loginSelenium(driver):
    #loads the page
    driver.get(ROOT + "/user_session/new?continue=%2F")
    
    #finds the login form
    loginForm = driver.find_element(By.ID, "new_user_session")
    
    #fills the form in
    loginForm.find_element(By.ID, "user_session_username_or_email").send_keys(username)
    loginForm.find_element(By.ID, "user_session_password").send_keys(password)
    
    time.sleep(0.1)
    #sumbits the form
    loginForm.find_element(By.XPATH, '//input[@type="submit"]').click()
    
    

def prepareSelenium():    
    driver = setupSelenium()
    loginSelenium(driver)
    return driver
    
def stopSelenium(driver):
    driver.quit()
    
               
if __name__ == "__main__":
    import settings
    import questions
    driver = prepareSelenium()
    id = input("please enter tournament id:")
    findTournament(driver, id)
    input()
    driver.quit()
