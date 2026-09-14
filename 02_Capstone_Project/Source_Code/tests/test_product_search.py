from config.config import BASE_URL
from data.test_data import PRODUCT_NAME
from pages.product_page import ProductPage


def test_product_search(driver):

    # Open TutorialsNinja
    driver.get(BASE_URL)

    print("TutorialsNinja home page opened.")

    # Create Product Page object
    product_page = ProductPage(driver)

    # Search using centralized test data
    product_page.search_product(PRODUCT_NAME)

    print("Product search completed.")

    # Get product name
    product_name = product_page.get_product_name()

    print("Product found:", product_name)

    # Verify product
    assert PRODUCT_NAME in product_name

    print("Product search test completed successfully.")