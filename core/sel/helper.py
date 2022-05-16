import sys
import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def fillInFormSelenium(driver, form, values):
    """
    Fills in the given form according to values.
    
    Values is a dictionary with key representing the target element's name and value it's requested value.
    """
    for value in values:
        
        try:
        
            element = form.find_element(By.XPATH, f".//*[@name='{value}']")
            
            # if the value is Bool, the target element is a switch
            if isinstance(values[value], bool):
                
                #the current value is different from the expected one
                if element.is_selected() != values[value]:
                
                    #the element is often unclickable, hence we have to use js
                    driver.execute_script("arguments[0].click()", element)
                    
                    with open("log", "a") as log:
                        print(f"{value} changed to {values[value]}", file=log)
            
            if isinstance(values[value], str) or isinstance(values[value], int):
                if element.get_attribute("value") != values[value]:
                    driver.execute_script("arguments[0].value = arguments[1]", element, values[value])
                    
                    
        except Exception as e:
            with open("log", "a") as log:
                print(e, file=log)
                
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