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

    @login
    Scenario: Login with invalid email and valid password credentials
        Given I navigate to Login page
        When I enter invalid email "test_auto1@gmail.com" address and valid password "12345" into the fields
        And I click on Login button
        Then I shoud get a proper warning message

    @login
    Scenario: Login with valid email and invalid password credentials
        Given I navigate to Login page
        When I enter valid email address "test_auto@gmail.com" and invalid password "123456" into the fields
        And I click on Login button
        Then I shoud get a proper warning message
    
    @login
    Scenario: Login with invalid credentials
        Given I navigate to Login page
        When I enter invalid email address "test_auto1@gmail.com" and invalid password "123456" into the fields
        And I click on Login button
        Then I shoud get a proper warning message

    @login
    Scenario: Login without entering any credentials
        Given I navigate to Login page
        When I don't enter anything into email and password fields
        And I click on Login button
        Then I shoud get a proper warning message