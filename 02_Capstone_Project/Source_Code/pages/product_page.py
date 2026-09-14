from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.search_box = (
            By.NAME,
            "search"
        )

        self.search_button = (
            By.CSS_SELECTOR,
            "button.btn.btn-default.btn-lg"
        )

        self.product_name = (
            By.XPATH,
            "//div[contains(@class, 'product-thumb')]//h4/a"
        )

        self.add_to_cart_button = (
            By.ID,
            "button-cart"
        )

        self.success_message = (
            By.CSS_SELECTOR,
            "div.alert.alert-success"
        )

        self.cart_link = (
            By.XPATH,
            "//a[contains(@href, 'checkout/cart')]"
        )

        self.cart_product_name = (
            By.XPATH,
            "//div[@id='content']//table//tbody//tr//td[2]/a"
        )

    def search_product(self, product_name):
        search = self.wait.until(
            EC.visibility_of_element_located(self.search_box)
        )

        search.clear()
        search.send_keys(product_name)

        self.wait.until(
            EC.element_to_be_clickable(self.search_button)
        ).click()

    def get_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.product_name)
        ).text

    def open_product(self):
        self.wait.until(
            EC.element_to_be_clickable(self.product_name)
        ).click()

    def add_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        ).click()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success_message)
        ).text

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()

    def get_cart_product_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.cart_product_name)
        ).text