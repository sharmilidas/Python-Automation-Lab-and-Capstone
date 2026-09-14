from config.config import BASE_URL
from data.test_data import LOGIN_EMAIL, LOGIN_PASSWORD
from pages.login_page import LoginPage


def test_valid_login(driver):

    # Open TutorialsNinja login page directly
    driver.get(
        BASE_URL + "index.php?route=account/login"
    )

    print("Login page opened successfully.")

    # Create Login Page object
    login_page = LoginPage(driver)

    # Login using centralized test data
    login_page.login(
        LOGIN_EMAIL,
        LOGIN_PASSWORD
    )

    # Verify successful login
    assert login_page.is_my_account_displayed()

    print("Login test completed successfully.")