from behave import given, when, then
from selenium.webdriver.common.by import By


@given("I open the SauceDemo login page")
def step_open_login_page(context):
    context.driver.get("https://www.saucedemo.com/")
    print("SauceDemo login page opened.")
    input("Take Screenshot 1 - Login Page, then press ENTER...")


@when('I enter username "{username}"')
def step_enter_username(context, username):
    context.driver.find_element(By.ID, "user-name").send_keys(username)


@when('I enter password "{password}"')
def step_enter_password(context, password):
    context.driver.find_element(By.NAME, "password").send_keys(password)


@when("I click the login button")
def step_click_login(context):
    context.driver.find_element(By.ID, "login-button").click()


@then("I should be redirected to the inventory page")
def step_verify_inventory_page(context):
    assert "/inventory.html" in context.driver.current_url
    print("Login successful.")
    print("Current URL:", context.driver.current_url)
    input("Take Screenshot 2 - Inventory Page, then press ENTER...")
    print("Selenium Python Behave BDD scenario completed successfully.")
