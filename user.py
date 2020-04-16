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

class account:
    '''
    Class that generates instances of account credentials, generate passwords and save information
    '''