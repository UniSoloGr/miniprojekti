
*** Settings ***
Library    Browser

*** Test Cases ***

Homepage Should Display Search Form
    New Browser    chromium    headless=True
    New Page    http://localhost:5001
    Get Text    h2:has-text("App")    ==    App
    Get Element    id=search-input
    Get Element    button[type="submit"]
    Get Element    a[href="/new_source"]
    Close Browser
