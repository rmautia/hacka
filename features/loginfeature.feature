@connectgui
Feature: Login to a page and assert welcome
  # Enter feature description here

  Scenario: User Logs in
    Given User navigate to the login page
    When User submit username and password
    Then User should be logged in
