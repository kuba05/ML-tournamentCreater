import sys
import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from core.helper import log

def applyValueOnForm(driver, element, value):
    if element.get_attribute("id") == "tournament_public_sign_up":
        print(driver.find_elements(By.ID, "tournament_public_sign_up"))
        print("IN")
        print(element.get_attribute("class"))
        print(element.get_attribute("type"))
        print(value)
        print(str(element.is_selected()) != str(value))
        input()
    if element.get_attribute("type") in ["radio", "checkbox"]:

        #the current value is different from the expected one        
        if str(element.is_selected()) != str(value):
            
            #the element is often unclickable, hence we have to use js
            driver.execute_script("arguments[0].click()", element)
            
            if str(element.is_selected()) != str(value):
                driver.execute_script("arguments[0].checked = arguments[1]", element, value)
        
            log(f"{element.get_attribute('id')} changed to {value}")
    
    else:
        if str(element.get_attribute("value")) != str(value):
            driver.execute_script("arguments[0].value = arguments[1]", element, value)
            
    
def fillInFormSelenium(driver, form, values):
    """
    Fills in the given form according to values.
    
    Values is a dictionary with key representing the target element's id and value its requested value.
    """
    for id in values:
        value = values[id]
        try:
            if isinstance(value, list):
            
                elements = form.find_elements(By.XPATH, f".//*[@id='{id}']")    
                for i in range(len(value)):
                    applyValueOnForm(driver, elements[i], value[i])
                    
                continue
            
            else:
            
                element = form.find_elements(By.XPATH, f".//*[@id='{id}']")[-1]
                applyValueOnForm(driver, element, value)
                
                
                
        except Exception as e:
            log("Exception in filling form: ", e, "\nThis error occured on id: ", id)
            
                
def submitFormSelenium(driver, form):
    time.sleep(0.1)
    button = form.find_element(By.XPATH, ".//input[@type='submit'][@name='commit']")
    
    try:
        # make the loading faster
        driver.set_page_load_timeout(10)
        driver.execute_script("arguments[0].click()", button)
    except TimeoutException:
        pass
        
    driver.set_page_load_timeout(300)
    
def loadPageSelenium(driver, URI):
    try:
        # make the loading faster
        driver.set_page_load_timeout(10)
        driver.get(URI)
    except TimeoutException:
        pass
        
    driver.set_page_load_timeout(300)