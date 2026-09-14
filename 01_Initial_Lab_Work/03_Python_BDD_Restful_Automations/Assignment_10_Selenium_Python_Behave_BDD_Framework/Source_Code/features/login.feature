Feature: SauceDemo login

  Scenario: Successful login with valid credentials
    Given I open the SauceDemo login page
    When I enter username "standard_user"
    And I enter password "secret_sauce"
    And I click the login button
    Then I should be redirected to the inventory page
