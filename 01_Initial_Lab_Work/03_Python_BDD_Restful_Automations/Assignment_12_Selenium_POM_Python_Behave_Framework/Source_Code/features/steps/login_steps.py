from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@given("I open the SauceDemo login page using the Login Page Object")
def step_open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()
    print("SauceDemo login page opened using LoginPage.")


@when('I login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)
    print("Login performed using LoginPage methods.")


@then("the SauceDemo inventory page should be displayed")
def step_verify_inventory(context):
    context.inventory_page = InventoryPage(context.driver)

    assert context.inventory_page.is_displayed()
    assert context.inventory_page.get_title() == "Products"

    print("Inventory page displayed successfully.")
    print("Page title:", context.inventory_page.get_title())
