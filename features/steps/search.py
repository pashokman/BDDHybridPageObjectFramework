from behave import *
from selenium import webdriver

from selenium.webdriver.common.by import By


@given(u'I got navigated to Home page')
def step_impl(context):
    expected_title = 'Your Store'
    current_title = context.driver.title

    assert expected_title == current_title, 'This is not a Home page'


@when(u'I enter valid product into the Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('HP')


@when(u'I click on Search button')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'input-group-btn').click()


@then(u'Valid product should be displayed in Search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'HP LP3065').is_displayed()


@when(u'I enter invalid product into the Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('Honda')


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    expected_message = 'There is no product that matches the search criteria.'
    current_message = context.driver.find_element(By.XPATH, '//div[@id="content"]//p[2]').text
    
    assert current_message== expected_message, 'Message does not match (Invalid product search)'


@when(u'I don\'t enter any product into the Search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, 'search').send_keys('')
