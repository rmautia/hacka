from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pytest_bdd import given, when, then, parsers
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

pytest_plugins = ["pytest_bdd"]

use_step_matcher("re")


@given("I am on the Google search page")
def go_to_google(context):
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.google.com")
    return driver


@when('I enter "Test Automation" into the search box')
def enter_search_term(driver, search_term="Test Automation"):
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_term)


@step("I click the search button")
def click_search_button(driver):
    search_button = driver.find_element(By.NAME, "btnK")
    search_button.click()


@then('I should see search results for "Test Automation"')
def verify_search_results(driver, search_term):
    assert search_term in driver.title