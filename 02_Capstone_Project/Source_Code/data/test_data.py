import os

from dotenv import load_dotenv


load_dotenv()

LOGIN_EMAIL = os.getenv("LOGIN_EMAIL")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")
PRODUCT_NAME = os.getenv("PRODUCT_NAME", "MacBook")