*** Settings ***
Resource    resource.robot
Test Setup    Open Application
Test Teardown    Close Application

*** Test Cases ***
Reject Future Year
    ${current_year}=    Evaluate    datetime.datetime.now().year    modules=datetime
    ${future_year}=    Evaluate    ${current_year} + 1
    Fill Required Fields    Test Source    Test Author    ${future_year}
    Submit Form
    Get Text    body    contains    Year cannot be in the future

Reject Negative Year
    Fill Required Fields    Test Source    Test Author    -2020
    Submit Form
    Get Text    body    contains    Year cannot be a negative number

Reject Empty Title
    Fill Required Fields    ${EMPTY}    Test Author    2020
    Submit Form
    Get Text    body    contains    Title and author are required

Reject Empty Author
    Fill Required Fields    Test Source    ${EMPTY}    2020
    Submit Form
    Get Text    body    contains    Title and author are required
