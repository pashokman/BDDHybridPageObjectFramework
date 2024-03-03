Feature: Login Functionality

    @login
    Scenario: Login with valid credentials
        Given I navigate to Login page
        When I enter valid email address and valid password into the fields
        And I click on Login button
        Then I shoud get logged in

    @login
    Scenario: Login with invalid email and valid password credentials
        Given I navigate to Login page
        When I enter invalid email address and valid password into the fields
        And I click on Login button
        Then I shoud get a proper warning message

    @login
    Scenario: Login with valid email and invalid password credentials
        Given I navigate to Login page
        When I enter valid email address and invalid password into the fields
        And I click on Login button
        Then I shoud get a proper warning message
    
    @login @completed
    Scenario: Login with invalid credentials
        Given I navigate to Login page
        When I enter invalid email address and invalid password into the fields
        And I click on Login button
        Then I shoud get a proper warning message

    @login
    Scenario: Login without entering any credentials
        Given I navigate to Login page
        When I don't enter anything into email and password fields
        And I click on Login button
        Then I shoud get a proper warning message