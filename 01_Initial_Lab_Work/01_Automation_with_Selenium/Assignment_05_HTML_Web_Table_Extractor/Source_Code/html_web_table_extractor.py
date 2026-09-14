from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the web table practice page
    driver.get("https://testautomationpractice.blogspot.com/")

    # Maximize the browser
    driver.maximize_window()

    print("Web Table page opened.")

    # Wait until the BookTable is visible
    wait = WebDriverWait(driver, 10)

    table = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//table[@name='BookTable']")
        )
    )

    print("BookTable found successfully.")

    # -------------------------------------------------
    # COUNT ROWS AND COLUMNS
    # -------------------------------------------------

    rows = table.find_elements(By.XPATH, ".//tr")
    headers = table.find_elements(By.XPATH, ".//tr[1]/th")

    print("Number of rows:", len(rows))
    print("Number of columns:", len(headers))

    # -------------------------------------------------
    # DISPLAY TABLE HEADERS
    # -------------------------------------------------

    print("\nTable Headers:")

    for header in headers:
        print(header.text, end=" | ")

    print("\n")

    # -------------------------------------------------
    # DISPLAY ALL TABLE DATA
    # -------------------------------------------------

    print("Complete Table Data:")

    for row in rows[1:]:

        columns = row.find_elements(By.XPATH, "./td")

        for column in columns:
            print(column.text, end=" | ")

        print()

    # -------------------------------------------------
    # FIND BOOKS WRITTEN BY MUKESH
    # -------------------------------------------------

    print("\nBooks written by Mukesh:")

    mukesh_found = False

    for row in rows[1:]:

        columns = row.find_elements(By.XPATH, "./td")

        if len(columns) >= 4:

            book_name = columns[0].text
            author = columns[1].text
            subject = columns[2].text
            price = columns[3].text

            if author.strip().lower() == "mukesh":

                print("Book Name:", book_name)
                print("Author:", author)
                print("Subject:", subject)
                print("Price:", price)
                print("-----------------------------")

                mukesh_found = True

    # Verify that at least one book by Mukesh was found
    assert mukesh_found, "No book written by Mukesh was found."

    print("Mukesh book search completed successfully.")
    print("Assignment 05 completed successfully.")

    # Keep browser open for screenshots
    input("Take the required screenshots, then press ENTER to close...")

finally:
    # Close the browser
    driver.quit()