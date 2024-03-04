from features.pages.SuccessfulLoginPage import SuccessfulLoginPage
from features.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    
    email_field_name = 'email'
    password_field_name = 'password'
    login_btn_xpath = '//input[@value="Login"]'
    warning_xpath = '//div[@class="alert alert-danger alert-dismissible"]'


    def enter_email_address(self, email):
        self.type_into_element('email_field_name', self.email_field_name, email)
    

    def enter_password(self, password):
        self.type_into_element('password_field_name', self.password_field_name, password)


    def enter_credentials(self, email, password):
        self.enter_email_address(email)
        self.enter_password(password)


    def click_on_login_btn(self):
        self.click_on_element('login_btn_xpath', self.login_btn_xpath)
        return SuccessfulLoginPage(self.driver)


    def get_warning(self):
        return self.retrive_element_text('warning_xpath', self.warning_xpath)
