from selenium import webdriver
from login_page import LoginPage


driver = webdriver.Chrome()

try:
    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    print("SauceDemo login page opened.")

    # -------------------------------------------------
    # SCREENSHOT 1 - LOGIN PAGE
    # -------------------------------------------------

    input("Take Screenshot 1 - Login Page, then press ENTER...")

    # Create Page Object
    login_page = LoginPage(driver)

    # Enter username
    login_page.enter_username("standard_user")

    # Enter password
    login_page.enter_password("secret_sauce")

    print("Username and password entered.")

    # Click Login
    login_page.click_login()

    print("Login button clicked.")

    # -------------------------------------------------
    # VERIFY LOGIN
    # -------------------------------------------------

    assert "/inventory.html" in driver.current_url

    print("Login successful.")
    print("Current URL:", driver.current_url)

    # -------------------------------------------------
    # SCREENSHOT 2 - INVENTORY PAGE
    # -------------------------------------------------

    input("Take Screenshot 2 - Inventory Page, then press ENTER...")

    # -------------------------------------------------
    # FINAL RESULT
    # -------------------------------------------------

    print("----------------------------------------")
    print("Page Object Model executed successfully.")
    print("Assignment 07 completed successfully.")
    print("----------------------------------------")

    # -------------------------------------------------
    # SCREENSHOT 3 - TERMINAL
    # -------------------------------------------------

    input("Take Screenshot 3 - Successful Execution, then press ENTER to close...")

finally:
    driver.quit()