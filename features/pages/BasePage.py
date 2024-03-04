from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_class_n"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        
        return element


    def get_elements(self, locator_name, locator_value):
        elements = []
        if locator_name.endswith("_xpath"):
            elements = self.driver.find_elements(By.XPATH, locator_value)
        elif locator_name.endswith("_id"):
            elements = self.driver.find_elements(By.ID, locator_value)
        elif locator_name.endswith("_name"):
            elements = self.driver.find_elements(By.NAME, locator_value)
        elif locator_name.endswith("_link_text"):
            elements = self.driver.find_elements(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_class_n"):
            elements = self.driver.find_elements(By.CLASS_NAME, locator_value)
        elif locator_name.endswith("_css"):
            elements = self.driver.find_elements(By.CSS_SELECTOR, locator_value)
        
        return elements
    

    def click_on_element(self, locator_name, locator_value):
        self.get_element(locator_name, locator_value).click()


    def type_into_element(self, locator_name, locator_value, text):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.clear()
        element.send_keys(text)


    def display_status_of_element(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.is_displayed()
    

    def retrive_element_text(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        return element.text
    

    def get_title(self):
        return self.driver.title


    def check_all_true(*args):
        return all(args)