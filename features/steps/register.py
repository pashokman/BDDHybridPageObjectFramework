from behave import *

from features.pages.AccountCreatedPage import AccountCreatedPage
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage


@given(u'I naviagte to Register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.click_on_register_option()


@when(u'I enter details into mandatory fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_mandatory_fields(
        'John', 'Doe', context.register_page.generate_email(), '1234567890', '12345')


@when(u'I select Privacy Policy option')
def step_impl(context):
    context.register_page.accept_on_privacy_policy_option()


@when(u'I click on Continue button')
def step_impl(context):
    context.register_page.click_on_continue_btn()


@then(u'Account should get created')
def step_impl(context):
    expected_message = 'Your Account Has Been Created!'
    context.account_created_page = AccountCreatedPage(context.driver)
    current_message = context.account_created_page.get_account_successfully_created_message()
    
    assert expected_message == current_message, \
        f'Accout created message does not match: {current_message}'


@when(u'I select Subscribe Yes option')
def step_impl(context):
    context.register_page.select_subscribe_option()


@when(u'I enter details into all fields except email field')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_mandatory_fields('John', 'Doe', '', '1234567890', '12345')


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    existing_address = 'test_auto@gmail.com'
    context.register_page.enter_email(existing_address)


@then(u'Proper warning about duplicate account should be displayed')
def step_impl(context):
    expected_warning = 'Warning: E-Mail Address is already registered!'
    current_warning = context.register_page.get_warning()
    
    assert expected_warning == current_warning, \
        f'Warning (duplicate account/email) does not match: {current_warning}'


@when(u'I don\'t enter anything into the fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_mandatory_fields('', '', '', '', '')


@then(u'Proper warning (Privacy Policy) and messages for every mandatory fields except Password Confirm should be displayed')
def step_impl(context):
    expected_warning = 'Warning: You must agree to the Privacy Policy!'
    current_warning = context.register_page.get_warning()

    expected_messages = context.register_page.get_error_messages()
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

    assert expected_warning == current_warning, \
        f'Warning (all fields are clear) does not match: {current_warning}'
    
    assert expected_fistname_message == current_fistname_message, \
        f'Firstname error message does not match: {current_fistname_message}'
    
    assert expected_lastname_message == current_lastname_message, \
        f'Lastname error message does not match: {current_lastname_message}'
    
    assert expected_email_message == current_email_message, \
        f'Email error message does not match: {current_email_message}'
    
    assert expected_telephone_message == current_telephone_message, \
        f'Telephone error message does not match: {current_telephone_message}'
    
    assert expected_password_message == current_password_message, \
        f'Password error message does not match: {current_password_message}'
