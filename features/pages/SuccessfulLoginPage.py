from features.pages.BasePage import BasePage


class SuccessfulLoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    expected_field_link_text = 'Edit your account information'


    def field_is_displayed_after_successful_login(self):
        return self.display_status_of_element('expected_field_link_text', self.expected_field_link_text)