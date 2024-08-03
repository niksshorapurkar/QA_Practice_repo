
Feature: OrangeHRM Login
  Scenario: Login to OrangeHRM with valid parameters
    Given Launch chrome browser
    When I open orangeHRM homepage
    And Enter the username "Admin" and password "admin123"
    And click on login button
    Then User must successfully login to the Dashboard page