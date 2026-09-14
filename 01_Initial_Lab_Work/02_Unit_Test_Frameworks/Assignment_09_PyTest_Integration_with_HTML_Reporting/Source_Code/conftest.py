import os
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    # Capture a screenshot automatically when a test fails.
    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        os.makedirs("Screenshots", exist_ok=True)
        screenshot_name = request.node.name.replace("[", "_").replace("]", "_")
        screenshot_path = os.path.join(
            "Screenshots",
            f"{screenshot_name}_FAILED.png"
        )
        driver.save_screenshot(screenshot_path)
        print(f"Failure screenshot saved: {screenshot_path}")

    driver.quit()


# Store test result information on the test node.
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
