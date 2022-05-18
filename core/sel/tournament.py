import time

from selenium.webdriver.common.by import By
from .helper import fillInFormSelenium, loadPageSelenium, submitFormSelenium
from config.config import ROOT 

    
def createTournamentSelenium(driver, settings, eventURL=None):
    
    if eventURL == None:
        eventURL = ""
    else:
        eventURL = "/events/" + eventURL
        
    # goes to the settings page of tournament
    loadPageSelenium(driver, ROOT + eventURL + "/tournaments/new")
    
    # finds the form
    form = driver.find_element(By.ID, "tournament_form")
    
    # set the settings
    fillInFormSelenium(driver, form, settings)
    
    URL = driver.find_element(By.XPATH, "//*[@name='tournament[url]']").get_attribute("value")
    
    # sumbit the form
    submitFormSelenium(driver, form)
    
    return URL
    #input("Please check the settings and e.g. set time! Then continue by pressing enter in this window.")

def deleteTournamentSelenium(driver, tournamentURI):
    loadPageSelenium(driver, ROOT + "/" + tournamentURI + "/settings")
    button = driver.find_element(By.XPATH, "//a[text()='Delete']")
    
    #confirm the deleting
    driver.execute_script("arguments[0].click()", button)
    alert = driver.switch_to.alert
    alert.accept()