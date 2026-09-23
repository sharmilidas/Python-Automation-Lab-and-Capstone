
# 🚀 Selenium Python Automation Framework

### Capstone Project | Python Automation Course

> A modular Selenium WebDriver automation framework built with **Python, PyTest, Unittest and Page Object Model (POM)** for end-to-end functional testing of the TutorialsNinja Demo application.

---

## 📌 Project Overview

This project demonstrates the development of a structured and maintainable **Selenium Python automation framework**.

The framework automates key e-commerce workflows of the **TutorialsNinja Demo** application and demonstrates industry-relevant automation concepts such as:

- Selenium WebDriver
- PyTest
- Python Unittest
- Page Object Model (POM)
- PyTest Fixtures
- Explicit Waits
- Centralized Test Data
- Centralized Configuration
- Failure Screenshot Capture
- HTML Test Reporting

The framework is designed to be **reusable, maintainable and scalable** for future automation requirements.

---

## 🌐 Application Under Test

**Application:** TutorialsNinja Demo

**URL:**  
https://tutorialsninja.com/demo/

---

# 🎯 Project Objectives

The primary objectives of this project are:

- Automate important functional workflows using Selenium WebDriver.
- Implement the Page Object Model design pattern.
- Integrate PyTest for test execution and reporting.
- Demonstrate Python's built-in Unittest framework.
- Implement reusable browser fixtures.
- Use explicit waits for reliable synchronization.
- Separate test data from test logic.
- Centralize application configuration.
- Capture screenshots automatically when tests fail.
- Generate an HTML test execution report.
- Build a clean and maintainable automation framework.

---

# 🧪 Automated Test Scenarios

| ID | Test Scenario | Framework | Status |
|---|---|---|---|
| TC01 | User Registration | PyTest | ✅ PASS |
| TC02 | Valid User Login | PyTest | ✅ PASS |
| TC03 | Product Search | PyTest | ✅ PASS |
| TC04 | Add Product to Cart | PyTest | ✅ PASS |
| TC05 | Cart Validation | PyTest | ✅ PASS |
| TC06 | User Logout | PyTest | ✅ PASS |
| TC07 | Product Search | Unittest | ✅ PASS |

### 📊 Execution Summary

| Metric | Result |
|---|---:|
| Total Automated Tests | **7** |
| Passed | **7** |
| Failed | **0** |
| Pass Percentage | **100%** |

---

# 🏗️ Framework Architecture

```text
                    ┌──────────────────────┐
                    │    Test Scenarios    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      PyTest /        │
                    │       Unittest       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Page Object Model  │
                    │        (POM)         │
                    └──────────┬───────────┘
                               │
                ┌──────────────┼──────────────┐
                ▼              ▼              ▼
          ┌──────────┐   ┌──────────┐   ┌──────────┐
          │ Selenium │   │  Config  │   │   Test   │
          │WebDriver │   │   Data   │   │ Utilities│
          └────┬─────┘   └──────────┘   └──────────┘
               │
               ▼
        ┌─────────────────┐
        │ TutorialsNinja  │
        │   Web App       │
        └─────────────────┘
````

---

# 📂 Project Structure

## 📂 Capstone Project Structure

```text
02_Capstone_Project/
│
├── Demonstration/
│
├── Project_Report/
│   └── Selenium_Python_Capstone_Project_Report.pdf
│
├── Reports/
│   └── pytest_report.html
│
├── Screenshots/
│
├── Source_Code/
│   ├── config/
│   ├── data/
│   ├── pages/
│   ├── tests/
│   │   └── unittest/
│   ├── utils/
│   ├── conftest.py
│   ├── pytest.ini
│   └── requirements.txt
│
├── Test_Cases/
│
├── Test_Data/
│
└── Video_demonstration_link/
    └── README.md

---

# 🛠️ Technology Stack

| Technology            | Purpose                           |
| --------------------- | --------------------------------- |
| 🐍 Python             | Automation programming language   |
| 🌐 Selenium WebDriver | Browser automation                |
| 🧪 PyTest             | Test execution and fixtures       |
| 🔬 Unittest           | Python built-in testing framework |
| 📊 pytest-html        | HTML test reporting               |
| 🌎 Google Chrome      | Browser under test                |
| 💻 Visual Studio Code | Development environment           |
| 🛒 TutorialsNinja     | Application under test            |

---

# 🧩 Page Object Model

The framework follows the **Page Object Model (POM)** design pattern.

### `HomePage`

Responsible for:

* My Account navigation
* Registration navigation
* Login navigation

### `LoginPage`

Responsible for:

* Email input
* Password input
* Login action
* Login verification

### `RegisterPage`

Responsible for:

* Registration form
* User information entry
* Privacy Policy selection
* Account creation
* Registration verification

### `ProductPage`

Responsible for:

* Product search
* Product selection
* Add to Cart
* Shopping Cart navigation
* Cart product validation

### `AccountPage`

Responsible for:

* Account verification
* Logout
* Logout verification

---

# ⚙️ Framework Features

## 1. Selenium WebDriver

Selenium WebDriver is used to automate browser interactions and validate application behavior.

---

## 2. Page Object Model

Page-specific locators and actions are encapsulated inside dedicated page classes.

This provides:

* Better code organization
* Reduced duplication
* Easier maintenance
* Reusable page methods

---

## 3. PyTest Fixtures

The browser setup and cleanup are handled centrally through:

```text
Source_Code/conftest.py
```

The fixture:

1. Creates the Chrome browser.
2. Maximizes the window.
3. Provides the browser to the test.
4. Captures a screenshot if the test fails.
5. Closes the browser.

---

## 4. Explicit Waits

The framework uses Selenium's:

```python
WebDriverWait
```

along with expected conditions such as:

```python
visibility_of_element_located()
element_to_be_clickable()
```

This improves synchronization and avoids unnecessary fixed delays.

---

## 5. Centralized Configuration

The application URL is maintained in:

```text
Source_Code/config/config.py
```

Example:

```python
BASE_URL = "https://tutorialsninja.com/demo/"
```

This prevents the application URL from being duplicated across test files.

---

## 6. Centralized Test Data

Reusable test data is maintained in:

```text
Source_Code/data/test_data.py
```

Examples include:

* Login email
* Login password
* Product name

This makes test maintenance easier when test data changes.

---

## 7. Failure Screenshot Handling

The framework automatically captures screenshots when a PyTest test fails.

Screenshots are stored in:

```text
02_Capstone_Project/Screenshots/
```

This provides useful visual evidence for debugging and test analysis.

---

## 8. HTML Reporting

The framework uses:

```text
pytest-html
```

to generate a self-contained HTML test execution report.

Report location:

```text
02_Capstone_Project/Reports/pytest_report.html
```

---

# 📦 Installation

## Prerequisites

Make sure the following are installed:

* Python 3.x
* Google Chrome
* Visual Studio Code
* pip

Verify Python:

```bash
python --version
```

---

## Install Dependencies

Open a terminal inside:

```text
02_Capstone_Project/Source_Code
```

Run:

```bash
pip install -r requirements.txt
```

The required packages are:

```text
selenium
pytest
pytest-html
```

---

# ▶️ Running the Tests

## Run the Complete PyTest Suite

From:

```text
02_Capstone_Project/Source_Code
```

run:

```bash
python -m pytest -s
```

The complete suite executes all PyTest tests and generates the HTML report.

Expected result:

```text
6 passed
```

---

# 🔬 Running the Unittest Test

Run:

```bash
python -m unittest tests.unittest.test_product_search_unittest -v
```

Expected result:

```text
Ran 1 test

OK
```

---

# 📊 Test Execution Result

The final complete execution produced:

```text
7 passed in 57.65s
```

### Final Result

```text
╔══════════════════════════════════╗
║       AUTOMATION TEST RESULT     ║
╠══════════════════════════════════╣
║ Total Tests       : 7            ║
║ Passed            : 7            ║
║ Failed            : 0            ║
║ Pass Percentage   : 100%         ║
╚══════════════════════════════════╝
```

---

# 📑 Reports and Documentation

### Test Cases

Detailed test cases are available in:

```text
Test_Cases/Capstone_Test_Cases.md
```

### Project Report

The complete project report is available in:

```text
Project_Report/
```

### HTML Execution Report

The PyTest execution report is available in:

```text
Reports/pytest_report.html
```

### Screenshots

Execution screenshots are maintained in:

```text
Screenshots/
```

### Demonstration

Demonstration video/link will be maintained in:

```text
Demonstration/
```

---

# 🧪 Functional Workflow Coverage

The framework currently covers the following end-to-end workflows:

```text
User Registration
       ↓
User Login
       ↓
Product Search
       ↓
Product Selection
       ↓
Add to Cart
       ↓
Cart Validation
       ↓
User Logout
```

---

# 🔐 Test Data Note

The framework uses a dedicated test account for login and logout validation.

For a public GitHub repository, credentials should **not** be committed directly into source code.

For production-level implementation, sensitive values should be managed using:

* Environment variables
* `.env` files
* CI/CD secrets
* Secure credential management

---

# 📈 Future Enhancements

The framework can be extended with:

* 📊 CSV/Excel-based Data-Driven Testing
* 🌐 Cross-browser testing
* ⚡ Parallel test execution
* 📝 Advanced logging
* 📈 Enhanced reporting
* 🔄 Regression test suites
* 🤖 CI/CD integration
* 🔧 Environment-specific configuration
* 🧪 Additional negative test scenarios
* 🐳 Docker-based test execution

---

# 🎓 Learning Outcomes

This project demonstrates practical understanding of:

* Selenium WebDriver automation
* Python programming
* PyTest
* Unittest
* Page Object Model
* Fixtures
* Explicit synchronization
* Test data management
* Configuration management
* Failure handling
* HTML reporting
* Functional web automation

---

# 🏁 Conclusion

This capstone project successfully demonstrates the development of a structured and maintainable **Selenium Python automation framework**.

The framework combines **Selenium WebDriver, PyTest, Unittest and Page Object Model** to automate key TutorialsNinja workflows.

The final execution achieved:

> **7 automated tests passed with 0 failures — 100% pass rate.**

The modular architecture provides a strong foundation for extending the framework with additional test scenarios, data-driven execution, cross-browser support and CI/CD integration.

---

## 👨‍💻 Project

**Selenium Python Automation Framework**

**Course:** Python Automation
**Project Type:** Capstone Project
**Application:** TutorialsNinja Demo
**Automation Tool:** Selenium WebDriver
**Test Frameworks:** PyTest + Unittest
**Design Pattern:** Page Object Model

---

⭐ **Built as part of a Python Automation Capstone Project**

```



