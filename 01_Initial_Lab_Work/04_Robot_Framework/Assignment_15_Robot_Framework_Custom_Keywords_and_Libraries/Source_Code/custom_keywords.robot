*** Settings ***
Resource    resources/saucedemo_keywords.resource
Suite Teardown    Close SauceDemo Application


*** Test Cases ***
Custom Keywords Login Test
    Open SauceDemo Application
    Login To SauceDemo    standard_user    secret_sauce
    Verify Successful Login
    Logout From SauceDemo
