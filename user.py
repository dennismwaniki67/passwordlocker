import pyperclip
import random
class User:
    """
    Class that generates instances of users. 
    """
    user_list = [] # Empty contact list

    def __init__(self, first_name, last_name, password):
        '''
        __init__ method that will define properties for objects
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password   
        

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)  

    @classmethod
    def check_user(cls, first_name, password):
        '''
        Method checks if the name and  password entered matched the user_list[].
        '''
        current_user = ''
        for user in User.user_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user  

class Credentials:
    '''
    Class will generate instances of account and generate passwords while saving
    '''

    credentials_list = []
    users_credentials_list = []
    
    def __init__(self, user_name, site_name, account_name, password):
        '''
        define properties for our objects
        '''

        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password   
        
    def save_credential(self):
        '''
        this method stores credential objects in the credentials_list[]
        '''

        Credentials.credentials_list.append(self)  


    def generate_password(self):
        '''
        method to generate a password or create your own
        '''
        chars = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890^?!?$%&/()=?`'+#*'~';:_,.-<>|"
        password = ""

        length = int(input("[*] Input Password Length: "))
        while len(password) != length:
            password = password + random.choice(chars)
            if len(password) == length:
                print("Password: %s" % password)
        return password

    @classmethod
    def display_credentials(cls, user_name):
        '''
        method to show the list of credentials saved
        '''
        users_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                users_credentials_list.append(credential)
        return users_credentials_list

    
    def del_credential(self):
        '''
        deletes a saved credential from the credential_list
        '''
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def credential_exist(cls, site_name):
        '''
        checks if a credential exists from credential list.
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return True
        return False  


    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        method takes a site name and returns details that matches that site
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential

    @classmethod
    def copy_credential(cls, site_name):
        '''
        copies a credentials details after the credentials site_name has been entered
        '''
        find_credential = Credentials.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)
