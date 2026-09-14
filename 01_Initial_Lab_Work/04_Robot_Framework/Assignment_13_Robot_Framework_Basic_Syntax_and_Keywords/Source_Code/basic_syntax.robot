*** Settings ***
Library    SeleniumLibrary
Suite Teardown    Close All Browsers

*** Variables ***
${URL}       https://www.saucedemo.com/
${BROWSER}   Chrome
${USERNAME}  standard_user
${PASSWORD}  secret_sauce

*** Test Cases ***
Open Website And Login
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Page Should Contain Element    id=user-name
    Input Text    id=user-name    ${USERNAME}
    Input Text    id=password    ${PASSWORD}
    Click Button    id=login-button
    Wait Until Page Contains Element    id=inventory_container    10s
    Page Should Contain    Products
    Log    SauceDemo login and page verification completed successfully.
