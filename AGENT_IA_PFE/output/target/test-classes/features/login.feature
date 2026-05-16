Feature: Login functionality
  As a user I want to log in to the application So that I can access my account

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "admin@example.com"
    And I enter password "secret123"
    And I click the login button
    Then I should be redirected to the dashboard
    And I should see the welcome message "Welcome, Admin"

  Scenario: Failed login with wrong credentials
    Given I am on the login page
    When I enter username "wrong@example.com"
    And I enter password "wrongpassword"
    And I click the login button
    Then I should see an error message "Invalid credentials"
    And I should remain on the login page