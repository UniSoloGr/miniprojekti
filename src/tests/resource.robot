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