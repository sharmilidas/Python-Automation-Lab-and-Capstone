Feature: Data driven SauceDemo login

  Scenario Outline: Login using multiple test data sets
    Given I open the SauceDemo login page
    When I enter username "<username>"
    And I enter password "<password>"
    And I click the login button
    Then the login result should be "<expected_result>"

    Examples:
      | username      | password     | expected_result |
      | standard_user | secret_sauce | success         |
      | wrong_user    | wrong_pass   | failure         |
      | standard_user | wrong_pass   | failure         |
      | wrong_user    | secret_sauce | failure         |
