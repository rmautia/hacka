from behave import *
from common import environments
from gui import login_scenario

environment_util = environments.EnvironmentUtil()


@Given('User navigate to the login page')
def open_csv_portal(context):
    environment = context.config.userdata['env']
    if environment.lower() == 'stage':
        stage_values = environment_util.stage_environment_variables()
        context.driver = login_scenario.LoginPage().open_login_page(stage_values)
    elif environment.lower() == 'dev':
        dev_values = environment_util.dev_environment_variables()
        context.driver = login_scenario.LoginPage().open_login_page(dev_values)


@When('User submit username and password')
def give_creds(context):
    login_scenario.LoginPage().give_user_name_and_password(context.driver)


@Then('User should be logged in')
def assert_homepage(context):
    login_scenario.LoginPage().assert_home_page(context.driver)

