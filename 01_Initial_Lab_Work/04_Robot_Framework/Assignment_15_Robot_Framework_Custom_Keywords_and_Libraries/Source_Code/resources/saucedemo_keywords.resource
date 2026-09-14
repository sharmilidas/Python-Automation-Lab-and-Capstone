*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${URL}       https://www.saucedemo.com/
${BROWSER}   Chrome


*** Keywords ***
Open SauceDemo Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    id=user-name    10s

Login To SauceDemo
    [Arguments]    ${username}    ${password}
    Input Text    id=user-name    ${username}
    Input Text    id=password    ${password}
    Click Button    id=login-button

Verify Successful Login
    Wait Until Page Contains Element    id=inventory_container    10s
    Page Should Contain    Products

Logout From SauceDemo
    Click Button    id=react-burger-menu-btn
    Wait Until Element Is Visible    id=logout_sidebar_link    10s
    Click Element    id=logout_sidebar_link
    Wait Until Page Contains Element    id=login-button    10s

Close SauceDemo Application
    Close All Browsers
