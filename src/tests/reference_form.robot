*** Settings ***
Resource    resource.robot

*** Test Cases ***
Reference Form Should Display Fields
    Open Application
    Click    a[href="/new_source"]
    Get Element    id=reference_type
    Get Element    id=title
    Get Element    id=author
    Get Element    id=year
    Close Application

User Should Be Able To Add Custom Fields
    Open Application
    Click    a[href="/new_source"]
    Click    id=add-field
    Get Element Count    input[name="custom_field_names[]"]    ==    1
    Get Element Count    input[name="custom_field_values[]"]    ==    1
    Close Application