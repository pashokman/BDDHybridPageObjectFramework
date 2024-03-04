Feature: Register Account Functionality

    @register @one
    Scenario: Register with mandatory fields
        Given I naviagte to Register page
        When I enter below details into mandatory fields
            |firstname  |lastname   |telephone  |password   |
            |John       |Doe        |1234567890 |12345      |
        And I select Privacy Policy option
        And I click on Continue button
        Then Account should get created

    @register
    Scenario: Register with all fields
        Given I naviagte to Register page
        When I enter below details into mandatory fields
            |firstname  |lastname   |telephone  |password   |
            |John       |Doe        |1234567890 |12345      |
        And I select Subscribe Yes option
        And I select Privacy Policy option
        And I click on Continue button
        Then Account should get created

    @register
    Scenario: Register with duplicate email address
        Given I naviagte to Register page
        When I enter below details into all fields except email field
            |firstname  |lastname   |telephone  |password   |
            |John       |Doe        |1234567890 |12345      |
        And I enter existing accounts email "test_auto@gmail.com" into email field
        And I select Privacy Policy option
        And I click on Continue button
        Then Proper warning about duplicate account should be displayed
    
    @register
    Scenario: Register without providing any details
        Given I naviagte to Register page
        When I don't enter anything into the fields
        And I click on Continue button
        Then Proper warning (Privacy Policy) and messages for every mandatory fields except Password Confirm should be displayed
        