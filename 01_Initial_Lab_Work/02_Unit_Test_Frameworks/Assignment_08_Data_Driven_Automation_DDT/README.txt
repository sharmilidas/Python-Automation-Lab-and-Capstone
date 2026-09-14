Assignment 08 – Data-Driven Automation (DDT)

Module:
02_Unit_Test_Frameworks

Section:
2.1 Unittest

Website:
https://www.saucedemo.com/

Task:
Build a login script that reads multiple test cases from an external source
and executes combinations of correct and incorrect usernames and passwords,
asserting that the proper validation result appears for each.

External data source:
Source_Code/Test_Data/login_test_data.csv

Test cases:
TC01 - Correct username and password -> successful login
TC02 - Correct username and incorrect password -> validation error
TC03 - Incorrect username and correct password -> validation error
TC04 - Incorrect username and incorrect password -> validation error

Run:
Open a terminal inside Source_Code and run:

python data_driven_login.py

Screenshots:
Save execution screenshots in Source_Code/Screenshots/.
Recommended names:
1. 01_TC01_Successful_Login.png
2. 02_TC02_Validation_Error.png
3. 03_TC03_Validation_Error.png
4. 04_TC04_Validation_Error.png
5. 05_Successful_Execution.png
