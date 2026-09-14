from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the Selenium practice page
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    # Maximize the browser window
    driver.maximize_window()

    print("Automation Practice page opened.")

    # Pause so the initial page can be captured
    input("Screenshot 1: Take the initial page screenshot, then press ENTER...")

    # ---------------- CHECKBOXES ----------------

    # Select the first checkbox
    checkbox1 = driver.find_element(By.ID, "checkBoxOption1")

    if not checkbox1.is_selected():
        checkbox1.click()

    # Select the second checkbox
    checkbox2 = driver.find_element(By.ID, "checkBoxOption2")

    if not checkbox2.is_selected():
        checkbox2.click()

    # Verify that both checkboxes are selected
    assert checkbox1.is_selected()
    assert checkbox2.is_selected()

    print("Checkbox Option 1 selected:", checkbox1.is_selected())
    print("Checkbox Option 2 selected:", checkbox2.is_selected())

    # Pause so the selected checkboxes can be captured
    input("Screenshot 2: Take the checkbox screenshot, then press ENTER...")

    # ---------------- AUTOCOMPLETE / DYNAMIC DROPDOWN ----------------

    # Find the autocomplete input
    autocomplete = driver.find_element(By.ID, "autocomplete")

    # Type part of the country name
    autocomplete.send_keys("ind")

    # Wait until autocomplete suggestions are visible
    wait = WebDriverWait(driver, 10)

    suggestions = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, ".ui-menu-item div")
        )
    )

    # Loop through suggestions and select India
    country_selected = False

    for suggestion in suggestions:
        if suggestion.text.strip().lower() == "india":
            suggestion.click()
            country_selected = True
            break

    # Verify that India was selected
    assert country_selected
    assert autocomplete.get_attribute("value") == "India"

    print("Selected country:", autocomplete.get_attribute("value"))
    print("Autocomplete selection successful.")

    # Pause so the selected country can be captured
    input("Screenshot 3: Take the autocomplete screenshot, then press ENTER...")

    print("Assignment 03 completed successfully.")

    # Keep the browser open for final screenshot
    input("Take the final execution screenshot, then press ENTER to close...")

finally:
    # Close the browser
    driver.quit()
