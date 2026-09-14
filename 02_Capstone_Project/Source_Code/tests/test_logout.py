from config.config import BASE_URL
from data.test_data import LOGIN_EMAIL, LOGIN_PASSWORD
from pages.login_page import LoginPage
from pages.account_page import AccountPage


def test_logout(driver):

    # Open Login page
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

    print("User logged in successfully.")

    # Create Account Page object
    account_page = AccountPage(driver)

    # Verify account page
    assert account_page.is_account_page_displayed()

    print("Account page verified successfully.")

    # Logout
    account_page.logout()

    print("Logout completed successfully.")

    # Verify logout
    assert account_page.is_logout_successful()

    print("Logout verification successful.")
    print("Logout test completed successfully.")