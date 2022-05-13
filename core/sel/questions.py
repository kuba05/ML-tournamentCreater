from config.config import ROOT

def addQuestionWithSelenium(driver, **values):
    driver.get(ROOT+"")
    pass

def setQuestionsWithSelenium(driver, config):
    for value in config:
        addQuestion(driver, **value)
