from behave import *

from features.pages.HomePage import HomePage


@given("I naviagte to Register page")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page = context.home_page.click_on_register_option()


@when("I enter details into mandatory fields")
def step_impl(context):
    context.register_page.enter_mandatory_fields("John", "Doe", context.register_page.generate_email(), \
                                                 "1234567890", "12345")


@when("I select Privacy Policy option")
def step_impl(context):
    context.register_page.accept_on_privacy_policy_option()


@when("I click on Continue button")
def step_impl(context):
    context.account_created_page = context.register_page.click_on_continue_btn()


@then("Account should get created")
def step_impl(context):
    expected_message = "Your Account Has Been Created!"
    current_message = context.account_created_page.get_account_created_message()

    assert expected_message == current_message, f"Accout created message does not match: {current_message}"


@when("I select Subscribe Yes option")
def step_impl(context):
    context.register_page.select_subscribe_option()


@when("I enter details into all fields except email field")
def step_impl(context):
    context.register_page.enter_mandatory_fields("John", "Doe", "", "1234567890", "12345")


@when("I enter existing accounts email into email field")
def step_impl(context):
    existing_address = "test_auto@gmail.com"
    context.register_page.enter_email(existing_address)


@then("Proper warning about duplicate account should be displayed")
def step_impl(context):
    expected_warning = "Warning: E-Mail Address is already registered!"
    current_warning = context.register_page.get_warning()

    assert expected_warning == current_warning, f"Warning (duplicate account/email) does not match: {current_warning}"


@when("I don't enter anything into the fields")
def step_impl(context):
    context.register_page.enter_mandatory_fields("", "", "", "", "")


@then("Proper warning (Privacy Policy) and messages for every mandatory fields except Password Confirm should be displayed")
def step_impl(context):
    expected_warning = "Warning: You must agree to the Privacy Policy!"
    expected_fistname_message = "First Name must be between 1 and 32 characters!"
    expected_lastname_message = "Last Name must be between 1 and 32 characters!"
    expected_email_message = "E-Mail Address does not appear to be valid!"
    expected_telephone_message = "Telephone must be between 3 and 32 characters!"
    expected_password_message = "Password must be between 4 and 20 characters!"

    assert context.register_page.display_status_of_warnings_and_messages(
        expected_warning,
        expected_fistname_message,
        expected_lastname_message,
        expected_email_message,
        expected_telephone_message,
        expected_password_message,
    ), "Warning or message does not match"
