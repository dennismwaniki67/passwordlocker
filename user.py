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
        check_user Method checks if the name and  password entered matched the user_list.
        '''
        current_user = ''
        for user in User.user_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user  

class Account:
    '''
    Class that generates instances of account credentials, generate passwords and save information
    '''