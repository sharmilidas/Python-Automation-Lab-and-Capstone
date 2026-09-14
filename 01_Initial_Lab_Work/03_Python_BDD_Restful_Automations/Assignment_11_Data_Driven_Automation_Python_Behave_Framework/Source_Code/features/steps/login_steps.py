from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("I open the SauceDemo login page")
def step_open_login_page(context):
    context.driver.get("https://www.saucedemo.com/")


@when('I enter username "{username}"')
def step_enter_username(context, username):
    context.driver.find_element(By.ID, "user-name").send_keys(username)


@when('I enter password "{password}"')
def step_enter_password(context, password):
    context.driver.find_element(By.NAME, "password").send_keys(password)


@when("I click the login button")
def step_click_login(context):
    context.driver.find_element(By.ID, "login-button").click()


@then('the login result should be "{expected_result}"')
def step_verify_login_result(context, expected_result):
    if expected_result == "success":
        WebDriverWait(context.driver, 10).until(
            lambda driver: "/inventory.html" in driver.current_url
        )
        assert "/inventory.html" in context.driver.current_url
        print("Expected successful login verified.")
    else:
        error_message = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "h3[data-test='error']")
            )
        )
        assert error_message.is_displayed()
        print("Expected login failure verified.")

    print(
        f"Test data result '{expected_result}' verified successfully."
    )
