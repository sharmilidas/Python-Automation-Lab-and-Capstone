# Capstone Project – Test Cases

## Project
Selenium Python Framework Development using PyTest, Unittest and Page Object Model

## Application Under Test
TutorialsNinja Demo

---

## TC01 – User Registration

**Test Case ID:** TC01  
**Test Case Name:** Verify New User Registration  
**Module:** Registration  
**Priority:** High  

### Preconditions
- TutorialsNinja application is accessible.
- Browser is available.
- A unique email address is used.

### Test Steps
1. Open the TutorialsNinja application.
2. Navigate to My Account.
3. Select Register.
4. Enter first name.
5. Enter last name.
6. Enter a unique email address.
7. Enter telephone number.
8. Enter password.
9. Confirm password.
10. Accept the Privacy Policy.
11. Click Continue.

### Expected Result
The account should be created successfully and the "Your Account Has Been Created!" message should be displayed.

### Actual Result
Account was created successfully.

### Status
**PASS**

---

## TC02 – Valid User Login

**Test Case ID:** TC02  
**Test Case Name:** Verify Login with Valid Credentials  
**Module:** Login  
**Priority:** High  

### Preconditions
- A valid TutorialsNinja test account exists.

### Test Steps
1. Open the TutorialsNinja login page.
2. Enter the registered email address.
3. Enter the correct password.
4. Click Login.

### Expected Result
The user should be successfully logged in and the My Account page should be displayed.

### Actual Result
User logged in successfully and the My Account page was displayed.

### Status
**PASS**

---

## TC03 – Product Search

**Test Case ID:** TC03  
**Test Case Name:** Verify Product Search  
**Module:** Product Search  
**Priority:** Medium  

### Preconditions
- TutorialsNinja application is accessible.

### Test Steps
1. Open the TutorialsNinja home page.
2. Enter "MacBook" in the search box.
3. Click the Search button.
4. Retrieve the displayed product name.

### Expected Result
The search result should contain the requested product "MacBook".

### Actual Result
MacBook was displayed successfully in the search results.

### Status
**PASS**

---

## TC04 – Add Product to Cart

**Test Case ID:** TC04  
**Test Case Name:** Verify Product Can Be Added to Cart  
**Module:** Shopping Cart  
**Priority:** High  

### Preconditions
- TutorialsNinja application is accessible.
- MacBook product is available.

### Test Steps
1. Open the TutorialsNinja home page.
2. Search for "MacBook".
3. Open the MacBook product.
4. Click Add to Cart.
5. Read the confirmation message.

### Expected Result
The product should be added to the shopping cart and a success message should be displayed.

### Actual Result
MacBook was successfully added to the shopping cart.

### Status
**PASS**

---

## TC05 – Cart Validation

**Test Case ID:** TC05  
**Test Case Name:** Verify Added Product Appears in Cart  
**Module:** Shopping Cart  
**Priority:** High  

### Preconditions
- TutorialsNinja application is accessible.

### Test Steps
1. Search for "MacBook".
2. Open the MacBook product.
3. Add the product to the cart.
4. Open the shopping cart.
5. Retrieve the product name displayed in the cart.

### Expected Result
The shopping cart should contain the MacBook product.

### Actual Result
MacBook was displayed correctly in the shopping cart.

### Status
**PASS**

---

## TC06 – User Logout

**Test Case ID:** TC06  
**Test Case Name:** Verify User Logout  
**Module:** Logout  
**Priority:** High  

### Preconditions
- A valid user account exists.
- User credentials are valid.

### Test Steps
1. Open the TutorialsNinja login page.
2. Enter valid login credentials.
3. Click Login.
4. Verify the My Account page.
5. Perform logout.
6. Verify the Account Logout page.

### Expected Result
The user should be logged out successfully and the Account Logout page should be displayed.

### Actual Result
User was logged out successfully and logout was verified.

### Status
**PASS**

---

## TC07 – Product Search using Unittest

**Test Case ID:** TC07  
**Test Case Name:** Verify Product Search using Python Unittest  
**Module:** Unittest Integration  
**Priority:** Medium  

### Preconditions
- TutorialsNinja application is accessible.
- Selenium WebDriver is available.

### Test Steps
1. Initialize the Chrome browser using Unittest setUp().
2. Open the TutorialsNinja application.
3. Search for "MacBook" using the Product Page Object.
4. Retrieve the displayed product name.
5. Validate the product name using Unittest assertion.
6. Close the browser using tearDown().

### Expected Result
The product search should return MacBook and the Unittest assertion should pass.

### Actual Result
MacBook was found successfully and the Unittest execution completed successfully.

### Status
**PASS**

---

# Test Execution Summary

| Test Case ID | Test Case | Framework | Status |
|--------------|-----------|-----------|--------|
| TC01 | User Registration | PyTest | PASS |
| TC02 | Valid User Login | PyTest | PASS |
| TC03 | Product Search | PyTest | PASS |
| TC04 | Add Product to Cart | PyTest | PASS |
| TC05 | Cart Validation | PyTest | PASS |
| TC06 | User Logout | PyTest | PASS |
| TC07 | Product Search | Unittest | PASS |

**Total Test Cases:** 7  
**Passed:** 7  
**Failed:** 0  
**Pass Percentage:** 100%

---

# Framework Coverage

The test suite demonstrates:

- Selenium WebDriver
- Python
- PyTest
- Python Unittest
- Page Object Model
- PyTest Fixtures
- Explicit Waits
- Centralized Configuration
- Centralized Test Data
- Failure Screenshot Handling
- HTML Test Reporting
- Functional Web Automation