import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


from .helper import fillInFormSelenium, loadPageSelenium, submitFormSelenium

from core.helper import isLoggedIn, getLogin

from config.config import ROOT

username = None
password = None



def setupSelenium(headless = False):
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
    
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    
    if headless:
        options.add_argument("--headless")
    
    try:
        driver = webdriver.Chrome(executable_path = "core/sel/chromedriver.exe", service_log_path="log/selenium.log", options=options)
    except Exception as e:
        raise e
    return driver



def loginSelenium(driver):
    #loads the page
    loadPageSelenium(driver, ROOT + "/user_session/new?continue=%2F")
    #finds the login form
    loginForm = driver.find_element(By.XPATH, "//form[@id='new_user_session']")
    
    #fills the form in
    fillInFormSelenium(driver, loginForm,
        {
            "user_session[username_or_email]": username,
            "user_session[password]": password
        }
    )
    
    submitFormSelenium(driver, loginForm)
    
    

def prepareSelenium(headless = False):    
    driver = setupSelenium(headless)
    loginSelenium(driver)
    return driver
    
def stopSelenium(driver):
    driver.quit()
    
               
if __name__ == "__main__":
    import settings
    import questions
    driver = prepareSelenium()
    input()
    driver.quit()
