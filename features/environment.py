from selenium import webdriver
from utilities import ConfigReader


def before_scenario(context, driver):
    
    browser = ConfigReader.read_configuration('basic info', 'browser')
    
    if browser.lower() == 'chrome':
        context.driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        context.driver = webdriver.Firefox()
    elif browser.lower() == 'edge':
        context.driver = webdriver.Edge()
    
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration('basic info', 'url'))


def after_scenario(context, driver):
    context.driver.quit()