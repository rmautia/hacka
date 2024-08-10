@ggl
Feature: Google Search

  Scenario: Search for "Test Automation"
    Given I am on the Google search page
    When I enter "Test Automation" into the search box
    And I click the search button
    Then I should see search results for "Test Automation"
