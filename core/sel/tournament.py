import time

from selenium.webdriver.common.by import By
from .helper import applySettingsSelenium
from config.config import ROOT 

    
def CreateTournamentWithSelenium(driver, settings):
    
    # goes to the settings page of tournament
    try:
        # make the loading faster
        driver.set_page_load_timeout(10)
        driver.get(ROOT + f"/tournaments/new")
    except Exception as e:
        print(e)
        print("failed to load")
        pass
        
    # return to default
    driver.set_page_load_timeout(300)    
    
    # finds the form
    form = driver.find_element(By.ID, "tournament_form")
    
    # set the settings
    applySettingsSelenium(driver, form, settings)
    
    # sumbit the form
    btn = driver.find_element(By.XPATH, "//input[@value='Save and Continue']")
    time.sleep(0.1)
    driver.execute_script("arguments[0].click()", btn)
    input("Please check the settings and e.g. set time! Then continue by pressing enter in this window.")
