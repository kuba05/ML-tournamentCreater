import time

from selenium.webdriver.common.by import By
from .helper import fillInFormSelenium, loadPageSelenium, submitFormSelenium
from config.config import ROOT 

    
def createTournamentSelenium(driver, settings, eventURL=None):
    
    if eventURL != "":
        eventURL = "/events/" + eventURL
        
    # goes to the settings page of tournament
    loadPageSelenium(driver, ROOT + eventURL + "/tournaments/new")
    
    # finds the form
    form = driver.find_element(By.ID, "tournament_form")
    
    # set the settings
    fillInFormSelenium(driver, form, settings)
    
    input()
    
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
    time.sleep(0.1)
    
def addQuestionsSelenium(driver, tournamentURI, questions):
    for question in questions:
        loadPageSelenium(driver, ROOT + "/" + tournamentURI + "/form_fields/new")
        
        form = driver.find_element(By.ID, "new_form_field")
        
        question["form_field[choices]"]
        
def readTournamentSelenium(driver, tournamentURI, settings):
    loadPageSelenium(driver, ROOT + "/" + tournamentURI + "/settings")
    
    form = driver.find_element(By.ID, "tournament_form")
    
    output = {}
    for id in settings:
        try:
            e = form.find_elements(By.ID, id)[-1]
            if e.get_attribute("type") in ["radio", "checkbox"]:
                output[id] = e.is_selected()
            else:
                output[id] = e.get_attribute("value")
        except Exception:
            output[id]: None
    
    return output