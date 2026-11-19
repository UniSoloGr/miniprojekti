
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

Searching Unknown Source Should Show No Results
    New Browser    chromium    headless=True
    New Page    http://localhost:5001
    Fill Text    id=search-input    nonexistent-source-xyz123
    Click    button[type="submit"]
    Get Text    h3    ==    Search results
    Get Text    p    ==    No sources found.
    Close Browser
