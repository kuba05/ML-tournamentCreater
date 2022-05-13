import sys

from selenium.webdriver.common.by import By


def applySettingsSelenium(driver, form, settings):
    print(settings, file=sys.stderr)
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
                print("found string:", setting, file=sys.stderr)
                if element.get_attribute("value") != settings[setting]:
                    driver.execute_script("arguments[0].value = arguments[1]", element, settings[setting])
                    
                    
        except Exception as e:
            with open("log", "a") as log:
                print(e, file=log)
                
     