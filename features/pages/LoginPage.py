from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    
    name_field_name = 'email'
    password_field_name = 'password'
    login_btn_xpath = '//input[@value="Login"]'
    warning_xpath = '//div[@class="alert alert-danger alert-dismissible"]'


    def enter_email_address(self, email):
        self.driver.find_element(By.NAME, self.name_field_name).send_keys(email)
    
    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_field_name).send_keys(password)

    def enter_credentials(self, email, password):
        self.enter_email_address(email)
        self.enter_password(password)

    def click_on_login_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def get_warning(self):
        return self.driver.find_element(By.XPATH, self.warning_xpath).text
