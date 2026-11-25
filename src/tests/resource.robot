*** Settings ***
Library    Browser

*** Variables ***
${URL}    http://localhost:5001

*** Keywords ***
Open Application
    New Browser    chromium    headless=True
    New Page    ${URL}

Close Application
    Close Browser

Fill Required Fields
    [Arguments]    ${title}    ${author}    ${year}
    New Page    ${URL}/new_source
    Fill Text    input[name="title"]    ${title}
    Fill Text    input[name="author"]    ${author}
    Fill Text    input[name="year"]    ${year}

Submit Form
    Click    button[type="submit"]