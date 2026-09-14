Assignment 07 – Page Object Model (POM) Restructure

Module:
02_Unit_Test_Frameworks

Section:
2.3 Page Object Model

Website:
https://www.saucedemo.com/

Task:
Take the working Tier 1 Selenium script and restructure it into a Page Object
Model design.

Architecture:
- login_page.py contains the LoginPage class.
- Locators and UI methods are kept inside LoginPage.
- test_login.py contains the actual test flow and assertion.
- The assertion is intentionally kept separate from the locators.

Files:
Source_Code/
├── Screenshots/
├── login_page.py
└── test_login.py

Run:
python test_login.py

Screenshots to capture:
1. 01_Login_Page.png
2. 02_Inventory_Page.png
3. 03_Successful_Execution.png
