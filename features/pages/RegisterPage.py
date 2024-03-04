from datetime import datetime

from features.pages.AccountCreatedPage import AccountCreatedPage
from features.pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    firstname_name = 'firstname'
    lastname_name = 'lastname'
    email_name = 'email'
    telephone_name = 'telephone'
    password_name = 'password'
    confirm_password_name = 'confirm'
    privacy_policy_option_name = 'agree'
    continue_btn_xpath = '//input[@value="Continue"]'
    subscripe_yes_option_xpath = '//input[@name="newsletter"][@value=1]'
    warning_xpath = '//div[@class="alert alert-danger alert-dismissible"]'
    error_messages_xpath = '//div[@class="text-danger"]'


    @staticmethod
    def generate_email():
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        address = "test_auto" + time_stamp + "@gmail.com"
        return address
    

    def enter_firstname(self, firstname):
        self.type_into_element('firstname_name', self.firstname_name, firstname)


    def enter_lastname(self, lastname):
        self.type_into_element('lastname_name', self.lastname_name, lastname)


    def enter_email(self, email):
        self.type_into_element('email_name', self.email_name, email)


    def enter_telephone(self, telephone):
        self.type_into_element('telephone_name', self.telephone_name, telephone)


    def enter_password(self, password):
        self.type_into_element('password_name', self.password_name, password)


    def enter_confirm_password(self, password):
        self.type_into_element('confirm_password_name', self.confirm_password_name, password)


    def enter_mandatory_fields(self, firstname, lastname, email, telephone, password):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_confirm_password(password)


    def accept_on_privacy_policy_option(self):
        self.click_on_element('privacy_policy_option_name', self.privacy_policy_option_name)


    def click_on_continue_btn(self):
        self.click_on_element('continue_btn_xpath', self.continue_btn_xpath)
        return AccountCreatedPage(self.driver)


    def select_subscribe_option(self):
        self.click_on_element('subscripe_yes_option_xpath', self.subscripe_yes_option_xpath)


    def get_warning(self):
        return self.retrive_element_text('warning_xpath', self.warning_xpath)


    def get_error_messages(self):
        return self.get_elements('error_messages_xpath', self.error_messages_xpath)


    def display_status_of_warnings_and_messages(self, expeceted_warning, expected_fistname_message, \
                                                expected_lastname_message, expected_email_message, \
                                                expected_telephone_message, expected_password_message):
        
        privacy_status = self.get_warning().__contains__(expeceted_warning)
        
        err_messages_list = self.get_error_messages()
        firstname_status = err_messages_list[0].text.__eq__(expected_fistname_message)
        lastname_status = err_messages_list[1].text.__eq__(expected_lastname_message)
        email_status = err_messages_list[2].text.__eq__(expected_email_message)
        telephone_status = err_messages_list[3].text.__eq__(expected_telephone_message)
        password_status = err_messages_list[4].text.__eq__(expected_password_message)

        all_messages_present = self.check_all_true(privacy_status, firstname_status, lastname_status, 
                                                   email_status, telephone_status, password_status)
        
        return all_messages_present
