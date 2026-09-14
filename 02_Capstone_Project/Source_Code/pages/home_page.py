from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.my_account_link = (
            By.XPATH,
            "//a[contains(@title, 'My Account')]"
        )

        self.register_link = (
            By.LINK_TEXT,
            "Register"
        )

        self.login_link = (
            By.LINK_TEXT,
            "Login"
        )

    def open_my_account(self):
        self.wait.until(
            EC.element_to_be_clickable(self.my_account_link)
        ).click()

    def open_register(self):
        self.wait.until(
            EC.element_to_be_clickable(self.register_link)
        ).click()

    def open_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_link)
        ).click()

    def get_title(self):
        return self.driver.title