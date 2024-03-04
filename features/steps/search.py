from behave import *

from features.pages.HomePage import HomePage


@given(u'I got navigated to Home page')
def step_impl(context):
    expected_title = 'Your Store'
    context.home_page = HomePage(context.driver)
    current_title = context.home_page.get_title()

    assert expected_title == current_title, f'This is not a Home page: {current_title}'


@when(u'I enter valid product into the Search box field')
def step_impl(context):
    context.home_page.search('HP')


@when(u'I click on Search button')
def step_impl(context):
    context.search_results_page = context.home_page.click_search_btn()


@then(u'Valid product should be displayed in Search results')
def step_impl(context): 
    assert context.search_results_page.is_displayed_valid_product(), 'Valid product does not displayed'


@when(u'I enter invalid product into the Search box field')
def step_impl(context):
    context.home_page.search('Honda')


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    expected_message = 'There is no product that matches the search criteria.'
    current_message = context.search_results_page.get_invalid_product_message()
    
    assert expected_message == current_message, \
        f'Message (Invalid product search) does not match: {current_message}'


@when(u'I don\'t enter any product into the Search box field')
def step_impl(context):
    context.home_page.search('')
