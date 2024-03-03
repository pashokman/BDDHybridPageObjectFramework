from selenium.webdriver.common.by import By


class SuccessfulLoginPage:

    def __init__(self, driver):
        self.driver = driver


    expected_field_link_text = 'Edit your account information'


    def field_is_displayed_after_successful_login(self):
        return self.driver.find_element(By.LINK_TEXT, self.expected_field_link_text).is_displayed()