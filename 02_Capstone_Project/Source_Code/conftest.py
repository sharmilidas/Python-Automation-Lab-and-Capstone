import os

import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):

    # Create Chrome browser
    driver = webdriver.Chrome()

    # Maximize browser window
    driver.maximize_window()

    # Give the browser to the test
    yield driver

    # Check whether the test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        # Create Screenshots folder if it does not exist
        screenshot_folder = "../Screenshots"
        os.makedirs(screenshot_folder, exist_ok=True)

        # Create screenshot name from test name
        screenshot_name = (
            request.node.name.replace("[", "_")
            .replace("]", "_")
            + "_FAILED.png"
        )

        screenshot_path = os.path.join(
            screenshot_folder,
            screenshot_name
        )

        # Capture screenshot
        driver.save_screenshot(screenshot_path)

        print(
            f"\nFailure screenshot saved: {screenshot_path}"
        )

    # Close browser
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        f"rep_{report.when}",
        report
    )