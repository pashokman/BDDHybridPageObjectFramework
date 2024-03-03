from behave import *
from selenium import webdriver

from selenium.webdriver.common.by import By


@given(u'I navigate to Login page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//a[@title="My Account"]').click()
    context.driver.find_element(By.LINK_TEXT, 'Login').click()


@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.NAME, 'email').send_keys('test_auto@gmail.com')
    context.driver.find_element(By.NAME, 'password').send_keys('12345')


@when(u'I click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//input[@value="Login"]').click()


@then(u'I shoud get logged in')
def step_impl(context):
    expected_field = 'Edit your account information'
    
    assert context.driver.find_element(By.LINK_TEXT, expected_field).is_displayed()


@when(u'I enter invalid email address and valid password into the fields')
def step_impl(context):
    context.driver.find_element(By.NAME, 'email').send_keys('test_auto1@gmail.com')
    context.driver.find_element(By.NAME, 'password').send_keys('12345')


@then(u'I shoud get a proper warning message')
def step_impl(context):
    expected_warning = 'Warning: No match for E-Mail Address and/or Password.'
    current_warning = context.driver.find_element(By.XPATH, '//div[@class="alert alert-danger alert-dismissible"]').text
    
    assert current_warning == expected_warning, 'Warning message does not match (invalid email/password)'


@when(u'I enter valid email address and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.NAME, 'email').send_keys('test_auto@gmail.com')
    context.driver.find_element(By.NAME, 'password').send_keys('123456')


@when(u'I enter invalid email address and invalid password into the fields')
def step_impl(context):
    context.driver.find_element(By.NAME, 'email').send_keys('test_auto1@gmail.com')
    context.driver.find_element(By.NAME, 'password').send_keys('123456')


@when(u'I don\'t enter anything into email and password fields')
def step_impl(context):
    context.driver.find_element(By.NAME, 'email').send_keys('')
    context.driver.find_element(By.NAME, 'password').send_keys('')