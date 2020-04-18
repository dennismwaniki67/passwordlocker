#!/usr/bin/env python3.6
import pyperclip
from test import User, Credential

def create_user(fname, lname, password):
    '''
    Function will create a new user details.
    '''
    new_user = User(fname, lname, password)
    return new_user

def save_user(user):
    '''
    function to save new user account.
    '''
    User.save_user(user)
    
def verify_user(first_name, password):
    '''
    Function that verifies if user exists.
    '''
    checking_user = User.check_user(first_name, password)
    return checking_user    
