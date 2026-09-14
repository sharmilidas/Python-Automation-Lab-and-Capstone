from config.config import BASE_URL
from data.test_data import PRODUCT_NAME
from pages.product_page import ProductPage


def test_cart_validation(driver):

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

    # Open shopping cart
    product_page.open_cart()

    print("Shopping cart opened.")

    # Get product name from cart
    cart_product = product_page.get_cart_product_name()

    print("Product in cart:", cart_product)

    # Verify product
    assert cart_product == PRODUCT_NAME

    print("Cart product validation successful.")
    print("Cart Validation test completed successfully.")