#!/usr/bin/env python3.6
import pyperclip
from test import User, Credentials

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
    function to verify  user account.
    '''
    checking_user = User.check_user(first_name, password)
    return checking_user 

def generate_password(self):
    '''
    Fucntion that generates password.
    '''
    gen_password = Credentials.generate_password(self)
    return gen_password
    
def create_credential(user_name, site_name, account_name, password):
    '''
    Function that creates new credentials.
    '''
    new_credential = Credentials(user_name, site_name, account_name, password)
    return new_credential


