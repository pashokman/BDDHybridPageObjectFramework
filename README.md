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
10. Create hooks in ```features``` package in ```environment.py``` file - ```before_scenario, after_scenario```, for delete duplicated code from steps files.
11. Create ConfigReader.py utility in utilities package.
```
from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read('configuration/config.ini')
    return config.get(category, key)
```
12. Create ```configurations``` package in root folder and ```config.ini``` file inside of it.
```
[basic info]
browser = firefox
url = 'https://tutorialsninja.com/demo/'
```
13. Change ```environment.py``` file to work with ```config.ini``` file through the ConfigReader utility.