#!/usr/bin/env python3.6
import pyperclip
from test import User, Credential

def create_user(fname, lname, password):
    '''
    Function that creates a new user account.
    '''
    new_user = User(fname, lname, password)
    return new_user