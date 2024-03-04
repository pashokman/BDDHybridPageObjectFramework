from datetime import datetime
from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver


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
        self.driver.find_element(By.NAME, self.firstname_name).send_keys(firstname)
    
    def enter_lastname(self, lastname):
        self.driver.find_element(By.NAME, self.lastname_name).send_keys(lastname)
    
    def enter_email(self, email):
        self.driver.find_element(By.NAME, self.email_name).send_keys(email)
    
    def enter_telephone(self, telephone):
        self.driver.find_element(By.NAME, self.telephone_name).send_keys(telephone)
    
    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_name).send_keys(password)
    
    def enter_confirm_password(self, password):
        self.driver.find_element(By.NAME, self.confirm_password_name).send_keys(password)

    def enter_mandatory_fields(self, firstname, lastname, email, telephone, password):
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_confirm_password(password)

    def accept_on_privacy_policy_option(self):
        self.driver.find_element(By.NAME, self.privacy_policy_option_name).click()

    def click_on_continue_btn(self):
        self.driver.find_element(By.XPATH, self.continue_btn_xpath).click()

    def select_subscribe_option(self):
        self.driver.find_element(By.XPATH, self.subscripe_yes_option_xpath).click()

    def get_warning(self):
        return self.driver.find_element(By.XPATH, self.warning_xpath).text
    
    def get_error_messages(self):
        return self.driver.find_elements(By.XPATH, self.error_messages_xpath)
    
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

        if privacy_status and firstname_status and lastname_status and \
            email_status and telephone_status and password_status:
            return True
        else:                            
            return False


