from datetime import datetime
from behave import *
from selenium import webdriver

from selenium.webdriver.common.by import By


@given(u'I naviagte to Register page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//a[@title="My Account"]').click()
    context.driver.find_element(By.LINK_TEXT, 'Register').click()


@when(u'I enter details into mandatory fields')
def step_impl(context):
    context.driver.find_element(By.NAME, 'firstname').send_keys('John')
    context.driver.find_element(By.NAME, 'lastname').send_keys('Doe')
    
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    address = "test_auto" + time_stamp + "@gmail.com"
    
    context.driver.find_element(By.NAME, 'email').send_keys(address)
    context.driver.find_element(By.NAME, 'telephone').send_keys('1234567890')
    context.driver.find_element(By.NAME, 'password').send_keys('12345')
    context.driver.find_element(By.NAME, 'confirm').send_keys('12345')


@when(u'I select Privacy Policy option')
def step_impl(context):
    context.driver.find_element(By.NAME, 'agree').click()


@when(u'I click on Continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//input[@value="Continue"]').click()


@then(u'Account should get created')
def step_impl(context):
    expected_message = 'Your Account Has Been Created!'
    current_message = context.driver.find_element(By.XPATH, '//div[@id="content"]/h1').text
    
    assert current_message == expected_message, 'Accout created message does not match'


@when(u'I select Subscribe Yes option')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//input[@name="newsletter"][@value=1]').click()


@when(u'I enter details into all fields except email field')
def step_impl(context):
    context.driver.find_element(By.NAME, 'firstname').send_keys('John')
    context.driver.find_element(By.NAME, 'lastname').send_keys('Doe')
    context.driver.find_element(By.NAME, 'telephone').send_keys('1234567890')
    context.driver.find_element(By.NAME, 'password').send_keys('12345')
    context.driver.find_element(By.NAME, 'confirm').send_keys('12345')


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    existing_address = 'test_auto@gmail.com'
    context.driver.find_element(By.NAME, 'email').send_keys(existing_address)


@then(u'Proper warning about duplicate account should be displayed')
def step_impl(context):
    expected_warning = 'Warning: E-Mail Address is already registered!'
    current_warning = context.driver.find_element(By.XPATH, '//div[@class="alert alert-danger alert-dismissible"]').text
    
    assert expected_warning == current_warning, 'Warning does not match (duplicate account/email)'


@when(u'I don\'t enter anything into the fields')
def step_impl(context):
    context.driver.find_element(By.NAME, 'firstname').send_keys('')
    context.driver.find_element(By.NAME, 'lastname').send_keys('')
    context.driver.find_element(By.NAME, 'email').send_keys('')
    context.driver.find_element(By.NAME, 'telephone').send_keys('')
    context.driver.find_element(By.NAME, 'password').send_keys('')
    context.driver.find_element(By.NAME, 'confirm').send_keys('')


@then(u'Proper warning (Privacy Policy) and messages for every mandatory fields except Password Confirm should be displayed')
def step_impl(context):
    expected_warning = 'Warning: You must agree to the Privacy Policy!'
    current_warning = context.driver.find_element(By.XPATH, '//div[@class="alert alert-danger alert-dismissible"]').text

    expected_messages = context.driver.find_elements(By.XPATH, '//div[@class="text-danger"]')
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
