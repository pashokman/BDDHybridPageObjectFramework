# BDDHybridPageObjectFramework

All test scenarios are describe in ```*.feature``` files and all scenatio steps in folder ```steps``` in files ```*.py```.

# Tests that I made:
1. Login
    * Login with valid credentials
    * Login with invalid email and valid password credentials
    * Login with valid email and invalid password credentials
    * Login with invalid credentials
    * Login without entering any credentials

2. Register
    * Register with mandatory fields
    * Register with all fields
    * Register with duplicate email address
    * Register without providing any details

3. Search
    * Search for a valid product
    * Search for invalid product
    * Search without entering any product

# How to develop BDD Page object Framework:
## Create scenarious and implement steps
1. Create package ```features``` in project root folder.
2. Create package ```steps``` in ```features``` package.
3. Create 'behave.ini' file in project root folder. Add code into a file:
```
[behave]
stdout_capture = false
stderr_capture = false
log_capture = false
```
4. Create ```*.feature``` files with test scenarious, like ```login.feature```.
5. Describe scenarious:
```
Feature: Login Functionality

    @login
    Scenario: Login with valid credentials
        Given I navigate to Login page
        When I enter valid email address and valid password into the fields
        And I click on Login button
        Then I shoud get logged in
```
6. Run created feature with command:
    * to run all features ```behave features```
    * to run 1 feature ```behave features/login.feature```
    * to run scenarious wich marked with tag ```behave features --tag=login```
7. After the run, in console we get code to implement in steps, like:
```
@given(u'I navigate to Login page')
def step_impl(context):
    raise NotImplementedError...
```
8. We should create file with same name with extension '.py' in steps package - ```login.py``` and paste code from console into it.
9. Should implement all steps in steps files and than run tests.

## Create hooks and utilities
10. Create hooks in ```features``` package in ```environment.py``` file - ```before_scenario, after_scenario```, for delete duplicated code from steps files.
11. Create ConfigReader.py utility in utilities package for add oportunity to get some main test parameters.
```
from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read('configuration/config.ini')
    return config.get(category, key)
```
12. Create ```configurations``` package in root folder and ```config.ini``` file inside of it, for add oportunity to get some main test parameters like browser, url...
```
[basic info]
browser = firefox
url = 'https://tutorialsninja.com/demo/'
```
13. Change ```environment.py``` file to work with ```config.ini``` file through the ConfigReader utility.

## Add Page Object Model into the project
14. Create package ```pages``` in ```features``` package.
15. Create page object files with elements locators and methods to work with them, import page object files into steps and use POM classes.
16. Delete creation of Page Objects in steps, where I can transfer object through the ```context```.\
Before
```
@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_credentials('test_auto@gmail.com', '12345')


@when(u'I click on Login button')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.click_on_login_btn()
```
After
```
@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_credentials('test_auto@gmail.com', '12345')


@when(u'I click on Login button')
def step_impl(context):
    context.login_page.click_on_login_btn()
```

17. Add return statements that should return the next Page Object in current Page Object.\
Before
```
def click_search_btn(self):
    self.driver.find_element(By.CLASS_NAME, self.search_btn_class_name).click()
```
After
```
def click_search_btn(self):
    self.driver.find_element(By.CLASS_NAME, self.search_btn_class_name).click()
    return SearchResultsPage(self.driver)
```

18. In steps we should set the method into variable, for transfer object through the ```context``` into next steps.\
Before
```
@when(u'I click on Search button')
def step_impl(context):
    context.home_page.click_search_btn()
```
After
```
@when(u'I click on Search button')
def step_impl(context):
    context.search_results_page = context.home_page.click_search_btn()
```

### Create Base Page class and implement in it most used methods.
19. Create BasePage class and inherit it in all other classes.
20. Implement main page methods in BasePage class - get_element, click_on_element, type_into_element, check_display_status_of_element, retrive_element_text...
21. Optimize child pages classes to call BasePage methods.

## Add DDT aproach in tests if necessary
### Data for all scenario
22. Change feature file by adding Examples data for testing.\
Before
```
Feature: Login Functionality

    @login @only
    Scenario: Login with valid credentials
        Given I navigate to Login page
        When I enter valid email address and valid password into the fields
        And I click on Login button
        Then I shoud get logged in
```
After
```
Feature: Login Functionality

    @login @only
    Scenario Outline: Login with valid credentials
        Given I navigate to Login page
        When I enter valid email address as "<email>" and valid password as "<password>" into the fields
        And I click on Login button
        Then I shoud get logged in
        Examples:
            |email                          |password       |
            |test_auto@gmail.com            |12345          |
            |amotoorisampleone@gmail.com    |secondone      |
            |amotoorisampletwo@gmail.com    |secondtwo      |
            |amotoorisamplethree@gmail.com  |secondthree    |
```

23. Change step in steps file for using Example data in tests.\
Before
```
@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    context.login_page.enter_credentials('test_auto@gmail.com', '12345')
```
After
```
@when(u'I enter valid email address as "{email}" and valid password as "{password}" into the fields')
def step_impl(context, email, password):
    context.login_page.enter_credentials(email, password)
```

### Data for a specific step
22. Change feature file by adding Examples data for testing.\
Before
```
Feature: Register Account Functionality

    @register
    Scenario: Register with mandatory fields
        Given I naviagte to Register page
        When I enter details into mandatory fields
        And I select Privacy Policy option
        And I click on Continue button
        Then Account should get created
```
After
```
Feature: Register Account Functionality

    @register
    Scenario: Register with mandatory fields
        Given I naviagte to Register page
        When I enter below details into mandatory fields
            |firstname  |lastname   |telephone  |password   |
            |John       |Doe        |1234567890 |12345      |
        And I select Privacy Policy option
        And I click on Continue button
        Then Account should get created
```

23. Change step in steps file for using Example data in tests.\
Before
```
@when("I enter below details into mandatory fields")
def step_impl(context):
    context.register_page.enter_mandatory_fields("John", "Doe", context.register_page.generate_email(), \
                                                "1234567890", "12345")
```
After
```
@when("I enter below details into mandatory fields")
def step_impl(context):
    for row in context.table:
        context.register_page.enter_mandatory_fields(row['firstname'], row['lastname'], \
                                                    context.register_page.generate_email(),
                                                    row['telephone'], row['password'])
```

## Add Allure reporting and screenshoot on failure functionality
24. To run the command for allure reporting for behave we shoul before install allure module:
```
pip install allure-behave
```
25. To run the tests and make report should use command (report folder will be automatically created):
```
behave -f allure_behave.formatter:AllureFormatter -o Reports/ features
```
26. To generate the report from files wich we got from tests run, we should run ```cmd``` from root project folder and run acommand:
```
allure serve Reports
```
27. For making screenshot on failure, we should add ```after_step``` method into the ```environment.py``` file.
```
def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
            name = 'failed_screenshot',
            attachment_type = AttachmentType.PNG)
```