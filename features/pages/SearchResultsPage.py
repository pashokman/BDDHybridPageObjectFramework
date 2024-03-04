from features.pages.BasePage import BasePage


class SearchResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    valid_product_link_text = 'HP LP3065'
    invalid_product_message_xpath = '//div[@id="content"]//p[2]'


    def is_displayed_valid_product(self):
        return self.display_status_of_element('valid_product_link_text', self.valid_product_link_text)


    def get_invalid_product_message(self):
        return self.retrive_element_text('invalid_product_message_xpath', self.invalid_product_message_xpath)
