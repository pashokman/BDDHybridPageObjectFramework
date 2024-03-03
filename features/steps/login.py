from behave import *

from features.pages.SuccessfulLoginPage import SuccessfulLoginPage
from features.pages.LoginPage import LoginPage
from features.pages.HomePage import HomePage


@given(u'I navigate to Login page')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_on_my_account()
    home_page.click_on_login_option()


@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_credentials('test_auto@gmail.com', '12345')


@when(u'I click on Login button')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_on_login_btn()


@then(u'I shoud get logged in')
def step_impl(context):
    success_login_page = SuccessfulLoginPage(context.driver)
    
    assert success_login_page.field_is_displayed_after_successful_login(), 'Field does not exist or another error'


@when(u'I enter invalid email address and valid password into the fields')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_credentials('test_auto1@gmail.com', '12345')


@then(u'I shoud get a proper warning message')
def step_impl(context):
    expected_warning = 'Warning: No match for E-Mail Address and/or Password.'
    login_page = LoginPage(context.driver)
    current_warning = login_page.get_warning()
    
    assert current_warning == expected_warning, 'Warning message does not match (invalid email/password)'


@when(u'I enter valid email address and invalid password into the fields')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_credentials('test_auto@gmail.com', '123456')


@when(u'I enter invalid email address and invalid password into the fields')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_credentials('test_auto1@gmail.com', '123456')


@when(u'I don\'t enter anything into email and password fields')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_credentials('', '')