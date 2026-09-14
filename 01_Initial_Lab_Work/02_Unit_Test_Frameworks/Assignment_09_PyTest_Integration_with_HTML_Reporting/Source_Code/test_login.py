from selenium.webdriver.common.by import By


def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.NAME, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "/inventory.html" in driver.current_url

    print("Valid login test passed.")

    input("Take Screenshot 1 - Successful Login, then press ENTER...")


def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.NAME, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    error_message = driver.find_element(
        By.CSS_SELECTOR, "h3[data-test='error']"
    )

    assert error_message.is_displayed()
    assert "Username and password do not match" in error_message.text

    print("Invalid login validation test passed.")

    input("Take Screenshot 2 - Validation Error, then press ENTER...")
