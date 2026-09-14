import unittest

from selenium import webdriver

from config.config import BASE_URL
from pages.product_page import ProductPage


class TestProductSearch(unittest.TestCase):

    def setUp(self):
        # Create Chrome browser
        self.driver = webdriver.Chrome()

        # Maximize browser window
        self.driver.maximize_window()

    def test_product_search(self):

        # Open TutorialsNinja
        self.driver.get(BASE_URL)

        print("TutorialsNinja home page opened.")

        # Create Product Page object
        product_page = ProductPage(self.driver)

        # Search for MacBook
        product_page.search_product("MacBook")

        print("MacBook searched successfully.")

        # Get product name
        product_name = product_page.get_product_name()

        print("Product found:", product_name)

        # Unittest assertion
        self.assertIn(
            "MacBook",
            product_name
        )

        print("Unittest product search completed successfully.")

    def tearDown(self):
        # Close browser
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()