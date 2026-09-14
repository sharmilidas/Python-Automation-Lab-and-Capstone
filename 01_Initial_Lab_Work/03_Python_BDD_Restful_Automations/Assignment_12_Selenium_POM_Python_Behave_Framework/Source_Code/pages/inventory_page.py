from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Page Object for the SauceDemo inventory page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.inventory_container = (By.ID, "inventory_container")
        self.page_title = (By.CLASS_NAME, "title")

    def is_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.inventory_container)
        ).is_displayed()

    def get_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.page_title)
        ).text
