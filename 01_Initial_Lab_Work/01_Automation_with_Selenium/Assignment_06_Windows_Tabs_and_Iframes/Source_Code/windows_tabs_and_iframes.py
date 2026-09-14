from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:
    # -------------------------------------------------
    # PART 1: HANDLE IFRAME
    # -------------------------------------------------

    driver.get("https://the-internet.herokuapp.com/iframe")
    driver.maximize_window()

    print("Iframe page opened.")

    wait = WebDriverWait(driver, 10)

    # Wait for the iframe and switch into it
    iframe = wait.until(
        EC.presence_of_element_located((By.ID, "mce_0_ifr"))
    )

    driver.switch_to.frame(iframe)

    editor = wait.until(
        EC.visibility_of_element_located((By.ID, "tinymce"))
    )

    print("Successfully switched into iframe.")
    print("Iframe text:", editor.text)

    input("Take Screenshot 1 - Iframe, then press ENTER...")

    # Switch back to the main page
    driver.switch_to.default_content()

    print("Switched back to the main page.")

    # -------------------------------------------------
    # PART 2: HANDLE NEW WINDOW / TAB
    # -------------------------------------------------

    driver.get("https://the-internet.herokuapp.com/windows")

    print("Windows page opened.")

    main_window = driver.current_window_handle

    # Click the link that opens a new window
    driver.find_element(
        By.XPATH, "//a[text()='Click Here']"
    ).click()

    print("New window/tab opened.")

    # Get all available window handles
    all_windows = driver.window_handles

    print("Number of windows:", len(all_windows))

    # Switch to the newly opened window
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(window)
            break

    # Wait until the new window title is available
    wait.until(
        lambda d: d.title == "New Window"
    )

    print("Switched to new window.")
    print("New window title:", driver.title)

    input("Take Screenshot 2 - New Window, then press ENTER...")

    # Close the new window
    driver.close()

    print("New window closed.")

    # Switch back to the original window
    driver.switch_to.window(main_window)

    print("Switched back to the original window.")
    print("Original window title:", driver.title)

    input("Take Screenshot 3 - Original Window, then press ENTER...")

    # Verify that we are back on the original page
    assert "Opening a new window" in driver.page_source

    print("----------------------------------------")
    print("Iframe, window and tab handling completed successfully.")
    print("Assignment 06 completed successfully.")
    print("----------------------------------------")

    input("Take Screenshot 4 - Successful Execution, then press ENTER to close...")

finally:
    driver.quit()
