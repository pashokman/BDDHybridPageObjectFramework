from behave import *

from features.pages.AccountCreatedPage import AccountCreatedPage
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage


@given(u'I naviagte to Register page')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_on_my_account()
    home_page.click_on_register_option()


@when(u'I enter details into mandatory fields')
def step_impl(context):
    register_page = RegisterPage(context.driver)
    register_page.enter_mandatory_fields('John', 'Doe', register_page.generate_email(), '1234567890', '12345')


@when(u'I select Privacy Policy option')
def step_impl(context):
    register_page = RegisterPage(context.driver)
    register_page.accept_on_privacy_policy_option()


@when(u'I click on Continue button')
def step_impl(context):
    register_page = RegisterPage(context.driver)
    register_page.click_on_continue_btn()


@then(u'Account should get created')
def step_impl(context):
    expected_message = 'Your Account Has Been Created!'
    account_created_page = AccountCreatedPage(context.driver)
    current_message = account_created_page.get_account_successfully_created_message()
    
    assert current_message == expected_message, 'Accout created message does not match'


@when(u'I select Subscribe Yes option')
def step_impl(context):
    register_page = RegisterPage(context.driver)
    register_page.select_subscribe_option()


@when(u'I enter details into all fields except email field')
def step_impl(context):
    register_page = RegisterPage(context.driver)
    register_page.enter_mandatory_fields('John', 'Doe', '', '1234567890', '12345')


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    existing_address = 'test_auto@gmail.com'
    register_page = RegisterPage(context.driver)
    register_page.enter_email(existing_address)


@then(u'Proper warning about duplicate account should be displayed')
def step_impl(context):
    expected_warning = 'Warning: E-Mail Address is already registered!'
    register_page = RegisterPage(context.driver)
    current_warning = register_page.get_warning()
    
    assert expected_warning == current_warning, 'Warning does not match (duplicate account/email)'


@when(u'I don\'t enter anything into the fields')
def step_impl(context):
    register_page = RegisterPage(context.driver)
    register_page.enter_mandatory_fields('', '', '', '', '')


@then(u'Proper warning (Privacy Policy) and messages for every mandatory fields except Password Confirm should be displayed')
def step_impl(context):
    expected_warning = 'Warning: You must agree to the Privacy Policy!'
    register_page = RegisterPage(context.driver)
    current_warning = register_page.get_warning()

    expected_messages = register_page.get_error_messages()
    expected_fistname_message = 'First Name must be between 1 and 32 characters!'
    current_fistname_message = expected_messages[0].text
    expected_lastname_message = 'Last Name must be between 1 and 32 characters!'
    current_lastname_message = expected_messages[1].text
    expected_email_message = 'E-Mail Address does not appear to be valid!'
    current_email_message = expected_messages[2].text
    expected_telephone_message = 'Telephone must be between 3 and 32 characters!'
    current_telephone_message = expected_messages[3].text
    expected_password_message = 'Password must be between 4 and 20 characters!'
    current_password_message = expected_messages[4].text

    assert expected_warning == current_warning, 'Warning does not match (all fields are clear)'
    assert expected_fistname_message == current_fistname_message, 'Firstname error message does not match'
    assert expected_lastname_message == current_lastname_message, 'Lastname error message does not match'
    assert expected_email_message == current_email_message, 'Email error message does not match'
    assert expected_telephone_message == current_telephone_message, 'Telephone error message does not match'
    assert expected_password_message == current_password_message, 'Password error message does not match'
