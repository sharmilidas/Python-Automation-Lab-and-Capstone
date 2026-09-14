from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.account_heading = (
            By.XPATH,
            "//h2[contains(text(), 'My Account')]"
        )

        self.logout_heading = (
            By.XPATH,
            "//h1[contains(text(), 'Account Logout')]"
        )

    def is_account_page_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.account_heading
            )
        ).is_displayed()

    def logout(self):
        self.driver.get(
            "https://tutorialsninja.com/demo/index.php?route=account/logout"
        )

    def is_logout_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.logout_heading
            )
        ).is_displayed()