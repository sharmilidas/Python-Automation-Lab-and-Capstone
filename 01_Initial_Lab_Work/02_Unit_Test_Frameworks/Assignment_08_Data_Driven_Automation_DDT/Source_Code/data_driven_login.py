import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CSV_FILE = "Test_Data/login_test_data.csv"


def read_test_data():
    """Read login test cases from the external CSV file."""
    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def run_login_test(driver, test_case):
    """Execute one login test case and verify the expected result."""

    username = test_case["username"]
    password = test_case["password"]
    expected_result = test_case["expected_result"]

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    print("\n----------------------------------------")
    print("Executing:", test_case["test_case"])
    print("Username:", username)
    print("Password:", password)
    print("Expected Result:", expected_result)

    # Enter test data
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)

    # Click Login
    driver.find_element(
        By.XPATH, "//input[@id='login-button']"
    ).click()

    wait = WebDriverWait(driver, 10)

    if expected_result == "success":

        # Verify successful login
        wait.until(
            EC.url_contains("/inventory.html")
        )

        assert "/inventory.html" in driver.current_url

        print("Result: Login successful.")
        print("Validation: Successful login verified.")

        input(
            "Take screenshot of successful login, then press ENTER..."
        )

    else:

        # Verify validation error
        error_message = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "h3[data-test='error']")
            )
        )

        assert error_message.is_displayed()
        assert error_message.text.strip() != ""

        print("Result: Login failed as expected.")
        print("Validation Error:", error_message.text)

        input(
            "Take screenshot of validation error, then press ENTER..."
        )


driver = webdriver.Chrome()

try:
    test_data = read_test_data()

    print("Data-Driven Login Automation Started.")
    print("Number of test cases:", len(test_data))

    passed = 0

    for test_case in test_data:
        run_login_test(driver, test_case)
        passed += 1

    print("\n========================================")
    print("Data-Driven Automation completed successfully.")
    print("Test cases executed:", len(test_data))
    print("Test cases passed:", passed)
    print("Assignment 08 completed successfully.")
    print("========================================")

    input(
        "Take Screenshot - Successful Execution, then press ENTER to close..."
    )

finally:
    driver.quit()
