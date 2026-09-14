from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the JavaScript Alerts page
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Maximize the browser window
    driver.maximize_window()

    print("JavaScript Alerts page opened.")

    # =====================================================
    # 1. JAVASCRIPT ALERT
    # =====================================================

    # Click the JS Alert button
    driver.find_element(
        By.XPATH,
        "//button[text()='Click for JS Alert']"
    ).click()

    # Wait until the Alert appears
    alert = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    print("JavaScript Alert is displayed.")
    input("Take Screenshot 1 - Alert, then press ENTER...")

    # Accept the Alert
    alert.accept()

    print("JavaScript Alert accepted successfully.")

    # =====================================================
    # 2. JAVASCRIPT CONFIRM
    # =====================================================

    # Click the JS Confirm button
    driver.find_element(
        By.XPATH,
        "//button[text()='Click for JS Confirm']"
    ).click()

    # Wait until the Confirm dialog appears
    confirm = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    print("JavaScript Confirm is displayed.")
    input("Take Screenshot 2 - Confirm, then press ENTER...")

    # Dismiss the Confirm dialog
    confirm.dismiss()

    print("JavaScript Confirm dismissed successfully.")

    # =====================================================
    # 3. JAVASCRIPT PROMPT
    # =====================================================

    # Click the JS Prompt button
    driver.find_element(
        By.XPATH,
        "//button[text()='Click for JS Prompt']"
    ).click()

    # Wait until the Prompt appears
    prompt = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    # Enter text into the Prompt
    prompt.send_keys("Selenium Automation")

    print("Text entered into JavaScript Prompt.")
    input("Take Screenshot 3 - Prompt with text, then press ENTER...")

    # Accept the Prompt
    prompt.accept()

    print("JavaScript Prompt accepted successfully.")

    # =====================================================
    # 4. VERIFY PROMPT RESULT
    # =====================================================

    # Wait for the result to become visible
    result = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "result")
        )
    )

    # Get the result text
    result_text = result.text

    print("Prompt result:", result_text)

    # Verify the result
    assert result_text == "You entered: Selenium Automation"

    print("Prompt result verified successfully.")

    # Screenshot of final result
    input("Take Screenshot 4 - Prompt Result, then press ENTER...")

    # =====================================================
    # 5. FINAL EXECUTION
    # =====================================================

    print("----------------------------------------")
    print("Alert, Confirm and Prompt handled successfully.")
    print("Assignment 04 completed successfully.")
    print("----------------------------------------")

    input("Take Screenshot 5 - Terminal, then press ENTER to close...")

finally:
    # Close the browser
    driver.quit()