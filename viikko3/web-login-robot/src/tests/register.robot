*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  moti
    Set Password  kalle123
    set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ss
    Set Password  kalle123
    set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  motivaatio
    Set Password  moti
    set Password Confirmation  moti
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  motivaatio
    Set Password  moti1234
    set Password Confirmation  moti1233
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  succregi
    Set Password  moti1234
    set Password Confirmation  moti1234
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  succregi
    Set Password  moti1234
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  failregi
    Set Password  moti1234
    set Password Confirmation  moti1235
    Submit Credentials
    Go To Login Page
    Set Username  failregi
    Set Password  moti1234
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
