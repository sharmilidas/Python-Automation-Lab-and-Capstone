Assignment 09 – PyTest Integration with HTML Reporting

Module:
02_Unit_Test_Frameworks

Section:
2.2 PyTest Framework

Website:
https://www.saucedemo.com/

Task:
Build a simple Selenium test using PyTest. Use a fixture for browser setup
and teardown, execute the test from the terminal, and generate an HTML report.
A screenshot is automatically captured when a test fails.

Structure:
Source_Code/
├── Screenshots/
├── conftest.py
└── test_login.py

Additional files:
├── Reports/
├── pytest.ini
└── requirements.txt

Installation:
pip install -r requirements.txt

Run:
pytest

The HTML report will be generated at:
Reports/pytest_report.html

For a more direct command:
pytest -v --html=Reports/pytest_report.html --self-contained-html

Screenshots:
- Successful login screenshot can be captured during the first test.
- Validation error screenshot can be captured during the second test.
- If a test fails, conftest.py automatically saves a failure screenshot
  in Source_Code/Screenshots/.
