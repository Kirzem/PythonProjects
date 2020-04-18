#!/usr/bin/python3
#
# Simple login system. Take username and password, login, then write to a text
# file. If user doesn't exist, allow them to create an account.    4/16/20


print('Enter your username: ')
username = input()

print('Hello, ' + username + '!')
print('Enter your password: ')
password = input()

if len(password) <= 4:
    print('Please choose a password longer than 4 characters.')
    
    
    
login_info = username + ':' + password    # make info neat to put into a file
print (login_info)

