from features.pages.BasePage import BasePage


class AccountCreatedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    account_created_message_xpath = '//div[@id="content"]/h1'


    def get_account_created_message(self):
        return self.retrive_element_text('account_created_message_xpath', self.account_created_message_xpath)