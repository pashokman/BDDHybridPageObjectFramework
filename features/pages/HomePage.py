from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
from features.pages.RegisterPage import RegisterPage
from features.pages.SearchResultsPage import SearchResultsPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    my_account_option_xpath = '//a[@title="My Account"]'
    login_option_link_text = 'Login'
    register_option_link_text = 'Register'
    search_name = 'search'
    search_btn_class_n = 'input-group-btn'


    def click_on_my_account(self):
        self.click_on_element('my_account_option_xpath', self.my_account_option_xpath)


    def click_on_login_option(self):
        self.click_on_element('login_option_link_text', self.login_option_link_text)
        return LoginPage(self.driver)


    def click_on_register_option(self):
        self.click_on_element('register_option_link_text', self.register_option_link_text)
        return RegisterPage(self.driver)
    

    def search(self, product):
        self.type_into_element('search_name', self.search_name, product)
    

    def click_search_btn(self):
        self.click_on_element('search_btn_class_n', self.search_btn_class_n)
        return SearchResultsPage(self.driver)