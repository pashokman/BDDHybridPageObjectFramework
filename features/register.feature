Feature: Register Account Functionality

    @register
    Scenario: Register with mandatory fields
        Given I naviagte to Register page
        When I enter details into mandatory fields
        And I select Privacy Policy option
        And I click on Continue button
        Then Account should get created

    @register
    Scenario: Register with all fields
        Given I naviagte to Register page
        When I enter details into mandatory fields
        And I select Subscribe Yes option
        And I select Privacy Policy option
        And I click on Continue button
        Then Account should get created

    @register
    Scenario: Register with duplicate email address
        Given I naviagte to Register page
        When I enter details into all fields except email field
        And I enter existing accounts email into email field
        And I select Privacy Policy option
        And I click on Continue button
        Then Proper warning about duplicate account should be displayed
    
    @register
    Scenario: Register without providing any details
        Given I naviagte to Register page
        When I don't enter anything into the fields
        And I click on Continue button
        Then Proper warning (Privacy Policy) and messages for every mandatory fields except Password Confirm should be displayed
        