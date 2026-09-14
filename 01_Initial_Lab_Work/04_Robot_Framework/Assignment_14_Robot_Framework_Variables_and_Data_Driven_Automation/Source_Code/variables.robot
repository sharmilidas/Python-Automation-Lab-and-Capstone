*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=${EXECDIR}/Test_Data/login_data.csv
Test Template    Login Test With Data
Suite Teardown    Close All Browsers


*** Variables ***
${URL}       https://www.saucedemo.com/
${BROWSER}   Chrome


*** Test Cases ***
Data Driven Login With ${username} And ${password} And ${expected_result}
    ${username}    ${password}    ${expected_result}


*** Keywords ***
Login Test With Data
    [Arguments]    ${username}    ${password}    ${expected_result}

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Input Text    id=user-name    ${username}
    Input Text    id=password    ${password}

    Click Button    id=login-button

    IF    '${expected_result}' == 'success'
        Wait Until Page Contains Element    id=inventory_container    10s
        Page Should Contain    Products
    ELSE
        Wait Until Page Contains Element    css:h3[data-test="error"]    10s
        Element Should Be Visible    css:h3[data-test="error"]
    END

    Log    ${username} - ${expected_result} verified successfully.

    Close Browser