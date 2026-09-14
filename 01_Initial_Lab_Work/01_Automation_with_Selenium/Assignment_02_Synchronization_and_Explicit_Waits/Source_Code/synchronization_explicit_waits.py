from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the dynamic loading page
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    # Maximize the browser window
    driver.maximize_window()

    print("Dynamic Loading page opened.")

    # Find and click the Start button
    start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_button.click()

    print("Start button clicked.")

    # Create an explicit wait with a maximum timeout of 10 seconds
    wait = WebDriverWait(driver, 10)

    # Wait until the "Hello World!" text becomes visible
    hello_text = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='finish']/h4")
        )
    )

    # Get the displayed text
    result_text = hello_text.text

    print("Displayed text:", result_text)

    # Verify the expected text
    assert result_text == "Hello World!"

    print("Text verification successful.")
    print("Assignment 02 completed successfully.")

    # Keep the browser open for screenshots
    input("Take the required screenshots, then press ENTER to close...")

finally:
    # Close the browser
    driver.quit()
