Assignment 12 - Selenium Page Object Model in Python Behave Framework

Objective:
Implement Selenium Page Object Model (POM) in a Python Behave BDD framework.

Application:
SauceDemo - https://www.saucedemo.com/

Architecture:
- pages/login_page.py contains login-page locators and actions.
- pages/inventory_page.py contains inventory-page verification.
- features/login.feature contains the business-readable scenario.
- features/steps/login_steps.py connects Gherkin steps with page objects.
- features/environment.py manages WebDriver setup and teardown.

Execution:
1. Open terminal in Source_Code.
2. Install dependencies:
   python -m pip install -r requirements.txt
3. Run:
   python -m behave

Screenshot:
Save the final terminal execution screenshot as:
01_Behave_POM_Execution.png
inside Source_Code/Screenshots.
