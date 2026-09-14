from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.email_field = (
            By.ID,
            "input-email"
        )

        self.password_field = (
            By.ID,
            "input-password"
        )

        self.login_button = (
            By.XPATH,
            "//input[@value='Login']"
        )

        self.my_account_heading = (
            By.XPATH,
            "//h2[contains(text(), 'My Account')]"
        )

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.email_field)
        ).send_keys(email)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.password_field)
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_my_account_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.my_account_heading
            )
        ).is_displayed()