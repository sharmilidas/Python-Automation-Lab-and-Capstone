from selenium.webdriver.common.by import By


class LoginPage:
    """Page Object for the SauceDemo login page."""

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//input[@id='login-button']")

    # UI methods
    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()