from behave import *

from features.pages.HomePage import HomePage
from features.pages.SearchResultsPage import SearchResultsPage


@given(u'I got navigated to Home page')
def step_impl(context):
    expected_title = 'Your Store'
    home_page = HomePage(context.driver)
    current_title = home_page.get_title()

    assert expected_title == current_title, 'This is not a Home page'


@when(u'I enter valid product into the Search box field')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.search('HP')


@when(u'I click on Search button')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_search_btn()


@then(u'Valid product should be displayed in Search results')
def step_impl(context):
    search_results_page = SearchResultsPage(context.driver)
    
    assert search_results_page.is_displayed_valid_product(), 'Valid product does not displayed'


@when(u'I enter invalid product into the Search box field')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.search('Honda')


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    expected_message = 'There is no product that matches the search criteria.'
    search_results_page = SearchResultsPage(context.driver)
    current_message = search_results_page.get_invalid_product_message()
    
    assert current_message == expected_message, 'Message does not match (Invalid product search)'


@when(u'I don\'t enter any product into the Search box field')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.search('')
