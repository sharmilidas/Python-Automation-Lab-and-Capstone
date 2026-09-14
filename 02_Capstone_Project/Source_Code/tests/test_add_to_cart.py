from config.config import BASE_URL
from data.test_data import PRODUCT_NAME
from pages.product_page import ProductPage


def test_add_to_cart(driver):

    # Open TutorialsNinja
    driver.get(BASE_URL)

    print("TutorialsNinja home page opened.")

    # Create Product Page object
    product_page = ProductPage(driver)

    # Search for product
    product_page.search_product(PRODUCT_NAME)

    print(f"{PRODUCT_NAME} searched successfully.")

    # Open product
    product_page.open_product()

    print(f"{PRODUCT_NAME} product opened.")

    # Add product to cart
    product_page.add_to_cart()

    print(f"{PRODUCT_NAME} added to cart.")

    # Get success message
    message = product_page.get_success_message()

    print("Success message:", message)

    # Verify success message
    assert "success" in message.lower()
    assert PRODUCT_NAME in message

    print("Add to Cart test completed successfully.")