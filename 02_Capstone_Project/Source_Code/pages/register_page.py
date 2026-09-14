from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.first_name = (
            By.ID,
            "input-firstname"
        )

        self.last_name = (
            By.ID,
            "input-lastname"
        )

        self.email = (
            By.ID,
            "input-email"
        )

        self.telephone = (
            By.ID,
            "input-telephone"
        )

        self.password = (
            By.ID,
            "input-password"
        )

        self.confirm_password = (
            By.ID,
            "input-confirm"
        )

        self.privacy_policy = (
            By.NAME,
            "agree"
        )

        self.continue_button = (
            By.XPATH,
            "//input[@value='Continue']"
        )

        self.success_heading = (
            By.XPATH,
            "//h1[contains(text(), 'Your Account Has Been Created!')]"
        )

    def enter_first_name(self, first_name):
        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.wait.until(
            EC.visibility_of_element_located(self.last_name)
        ).send_keys(last_name)

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.email)
        ).send_keys(email)

    def enter_telephone(self, telephone):
        self.wait.until(
            EC.visibility_of_element_located(self.telephone)
        ).send_keys(telephone)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.password)
        ).send_keys(password)

    def enter_confirm_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.confirm_password)
        ).send_keys(password)

    def accept_privacy_policy(self):
        self.wait.until(
            EC.element_to_be_clickable(self.privacy_policy)
        ).click()

    def click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def register(self, first_name, last_name, email, telephone, password):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_telephone(telephone)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.accept_privacy_policy()
        self.click_continue()

    def is_registration_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.success_heading
            )
        ).is_displayed()