Feature: SauceDemo login using Page Object Model

  Scenario: Successful login using reusable page objects
    Given I open the SauceDemo login page using the Login Page Object
    When I login with username "standard_user" and password "secret_sauce"
    Then the SauceDemo inventory page should be displayed
