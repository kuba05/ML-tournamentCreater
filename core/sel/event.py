def createAnEvent(driver):
    driver.get("https://challonge.com/events/new")
    
    applySettingsSelenium(driver, form, settings)