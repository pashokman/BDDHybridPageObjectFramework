from selenium.webdriver.common.by import By


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver


    valid_product_link_text = 'HP LP3065'
    invalid_product_message_xpath = '//div[@id="content"]//p[2]'


    def is_displayed_valid_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_product_link_text).is_displayed()
    
    def get_invalid_product_message(self):
        return self.driver.find_element(By.XPATH, self.invalid_product_message_xpath).text