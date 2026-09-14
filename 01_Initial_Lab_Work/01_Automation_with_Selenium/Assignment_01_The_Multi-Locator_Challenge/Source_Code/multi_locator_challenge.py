from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Create a Chrome WebDriver object
driver = webdriver.Chrome()

try:
    # Open the SauceDemo login page
    driver.get("https://www.saucedemo.com/")

    # Maximize the browser window
    driver.maximize_window()

    # Wait for you to take Screenshot 1
    print("Screenshot 1: Login page is displayed.")
    input("Take the screenshot, then press ENTER here...")

    # Find username using ID locator
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    # Find password using NAME locator
    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    # Find Login button using XPATH locator
    login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")

    # Click Login
    login_button.click()

    # Wait for the inventory page to load
    time.sleep(2)

    # Verify successful login
    assert "/inventory.html" in driver.current_url

    print("Login successful.")
    print("Current URL:", driver.current_url)

    # Wait for you to take Screenshot 2
    print("Screenshot 2: Inventory page is displayed.")
    input("Take the screenshot, then press ENTER here...")

    print("Assignment 01 completed successfully.")

    # Keep browser open until you press ENTER
    input("Press ENTER to close the browser...")

finally:
    driver.quit()