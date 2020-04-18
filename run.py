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

def save_credential(credential):
    '''
    Function to save a newly created credential.
    '''
    Credentials.save_credential(credential)

def display_credentials(username):
    '''
    Fucntion to display credentials saved.
    '''
    return Credentials.display_credential(username)   

def copy_credential(site_name):
    '''
    Function that copies credentials details to the clipborad.
    '''
    return Credentials.copy_credential(site_name)

def find_by_site(site_name):
    '''
    Function that searches for a site name.
    '''
    return Credentials.find_by_site_name(site_name)

def delete_credential(credential):
    '''
    Function that deletes credentials by site name.
    '''
    credential.del_credential()

def check_existing_credentials(site_name):
    '''
    Function that checks of a existing credential .
    '''
    return Credentials.credential_exist(site_name)

def main():
    print('\n')

    print("")
    print("HEYY U! Welcome to Password Locker System.")
    while True:
        print("*"*40)
        print('\n')
        print("Use these codes to navigate: \n ka - Create an account \n lg - Log in \n exit - Exit")
        print('\n')
        short_code = input("Enter a choice: ").lower().strip()

        if short_code == 'exit':
            break

        elif short_code == 'ka':
            print('\n')
            print("-"*40)
            print('\n')
            print("To create a new account:")
            first_name = input('Enter your first name - ').strip()
            last_name = input('Enter your last name - ').strip()
            password = input('Enter password - ').strip()
            save_user(create_user(first_name, last_name, password))
            print('\n')
            print(f"New account created for {first_name} {last_name} using password {password}")
        
        elif short_code == 'lg':
            print("-"*40)
            print('\n')
            print("Provide in your account details to log in.")
            user_name = input("Put in your first name - ").strip()
            password = str(input("Put in your password - "))
            user_exists = verify_user(user_name, password)
            if user_exists == user_name:
                print('\n')
                print(f"Welcome {user_name}. Kindly choose an option to continue.")
                while True:
                    print("-"*40)
                    print("Navigation codes: \n ca - To create a credential \n cd - To display all credentials \n cf - To find a credential \n cp - To copy password \n del - To delete a credential \n exit - Exit")
                    print('\n')
                    short_code = input('Enter a choice: ').lower().strip()
                    print("-"*40)
                    if short_code == 'ex':
                        print('\n')
                        print(f"Bye {user_name}")
                        break
                    elif short_code == 'ca':
                        print('\n')
                        print("Enter your credential details:")
                        site_name = input("Enter the site's name - ").strip()
                        account_name = input("Enter your account's username - ").strip()

                        while True:
                            print('\n')
                            print("-"*40)
                            print("Choose the password method you would like. Use keys: \n pe - To enter a password \n gp - To generate a password \n exit - Exit")
                            password_choice = input("Enter an option: ").lower().strip()
                            print("-"*40)
                            if password_choice == 'pe':
                                print('\n')
                                password = input("Enter your password: ").strip()
                                break
                            elif password_choice == 'gp':
                                password = generate_password(password)
                                break
                            elif password_choice == 'exit':
                                break
                            else:
                                print("OOPS! You entered the wrong option. Please try again.")
                        save_credential(create_credential(user_name, site_name, account_name,password))
                        print('\n')
                        print(f"Credential created: \n Site name: {site_name} - Account Username: {account_name} - Password: {password}")

                    elif short_code == 'cd':
                        print('\n')

                        if display_credentials(user_name):
                            print("Here is a list of all of your credentials:")
                            print('\n')
                            for credential in display_credentials(user_name):
                                print(f"Site name: {credential.site_name} - Account name: {credential.account_name} - Password: {credential.password}")
                        else:
                            print('\n')
                            print("You don't seem to have any credential saved yet.")
                            print('\n')


                    elif short_code == 'cf':
                        search_site = input("Enter the site name you are searching for: \n")
                        if check_existing_credentials(search_site):
                            result = find_by_site(search_site)
                            print(f"Search result: Site name: {result.site_name} - Account name: {result.account_name} - Password: {result.password}")
                        else:
                            print("No such credential exists. Please try again!")
                    
                    elif short_code == 'cp':
                        print('\n')
                        chosen_site = input("Enter the site name for the credential you want to copy: ")
                        copy_credential(chosen_site)
                        print('\n')
                    elif short_code == 'del':
                        print('\n')
                        print("Enter the name of the site credential you want to delete.")
                        print('\n')
                        answer = input("Enter choice: ")

                        if check_existing_credentials(answer):
                            answer = find_by_site(answer)
                            delete_credential(answer)
                            print("Credentials successfully deleted!")

                        else:
                            ("No such credential exists!")
                        
                    else:
                        print("OOPS! You entered the wrong option. Please try again.")
                
                else:
                    print('\n')
                    print("Bummer! You entered the wrong details Please try again or create an account.")

            else:
                print("-"*40)
                print('\n')
                print("I really didn't get that. Please use the short codes.")
if __name__ == '__main__':
    main()