def findTournamentWithSelenium(driver, tournamentURL):
    driver.get(ROOT + f"/{tournamentURL}")

    
def addjustSettingsWithSelenium(driver, tournamentURL, settings):
    
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