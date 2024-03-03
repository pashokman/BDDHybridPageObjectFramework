from selenium.webdriver.common.by import By


class AccountCreatedPage:

    def __init__(self, driver):
        self.driver = driver


    account_successfully_created_message_xpath = '//div[@id="content"]/h1'


    def get_account_successfully_created_message(self):
        return self.driver.find_element(By.XPATH, self.account_successfully_created_message_xpath).text