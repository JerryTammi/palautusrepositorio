*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  username  password1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  user  password1234
    Output Should Contain  User with username user already exists 

Register With Too Short Username And Valid Password
    Input Credentials  aa  password1234
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  user  moti123
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  user  motivaatio
    Output Should Contain  Password needs to contain numbers

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  user  password1234

