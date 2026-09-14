from config.config import BASE_URL
from pages.home_page import HomePage
from pages.register_page import RegisterPage

from datetime import datetime


def test_registration(driver):

    # Open TutorialsNinja
    driver.get(BASE_URL)

    # Create Home Page object
    home_page = HomePage(driver)

    # Open My Account
    home_page.open_my_account()

    # Open Register page
    home_page.open_register()

    # Create Register Page object
    register_page = RegisterPage(driver)

    # Test data
    first_name = "Surajit"
    last_name = "Test"
    email = f"surajit.test{datetime.now().strftime('%Y%m%d%H%M%S')}@example.com"
    telephone = "9876543210"
    password = "Test@12345"

    # Register the user
    register_page.register(
        first_name,
        last_name,
        email,
        telephone,
        password
    )

    # Verify registration
    assert register_page.is_registration_successful()

    print("Registration test completed successfully.")