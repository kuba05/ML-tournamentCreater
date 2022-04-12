from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

ROOT = "https://challonge.com"
username="testAccountMMM"
password="12345678"

def setup():
    """
    creates selenium driver and returns it
    """
    options = Options()
    options.binary_location = r'C:\Users\kuba\AppData\Local\Mozilla Firefox\firefox.exe'
    options.set_preference('permissions.default.stylesheet', 2)
    options.set_preference('permissions.default.image', 2)
    options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
    options.set_preference('javascript.enabled', False)
    driver = webdriver.Firefox(executable_path = "core/sel/firefoxDriver.exe", options=options)
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
    #goes to the settings page of tournament
    driver.get(ROOT + f"/{tournamentURL}/settings")
    print("got the site")
    form = driver.find_element(By.ID, "tournament_form")
    for setting in settings:
        print(f"working on {setting}")
        element = form.find_element(By.XPATH, f"//*[@name='{setting}']")
        if (element.is_selected()) != settings[setting]:
            element.click()
        
if __name__ == "__main__":
    driver = setup()
    login(driver)    
    id = input("please enter tournament id:")
    findTournament(driver, id)
    input()
    driver.quit()

def prepare():    
    driver = setup()
    login(driver)
    return driver
    
def stopSelenium(driver):
    input()
    driver.quit()