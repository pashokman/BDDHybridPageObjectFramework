from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    my_account_option_xpath = '//a[@title="My Account"]'
    login_option_link_text = 'Login'
    register_option_link_text = 'Register'
    search_name = 'search'
    search_btn_class_name = 'input-group-btn'


    def click_on_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_option_xpath).click()

    def click_on_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()

    def click_on_register_option(self):
        self.driver.find_element(By.LINK_TEXT, self.register_option_link_text).click()

    def get_title(self):
        return self.driver.title
    
    def search(self, product):
        self.driver.find_element(By.NAME, self.search_name).send_keys(product)
    
    def click_search_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.search_btn_class_name).click()