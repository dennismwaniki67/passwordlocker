import unittest # Importing the unittest module
from user import User,Account # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Dennis","Mwaniki","Mwaniki91") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Dennis")
        self.assertEqual(self.new_user.last_name,"Mwaniki")
        self.assertEqual(self.new_user.password,"Mwaniki91")
        
    def tearDown(self):
        '''
        A method that clears the users list after every test.
        '''
        User.user_list = []    

    def test_save_user(self):
        '''
        test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)
       
    def test_check_user(self):
        '''
        Test test_check_user case to test whether login feature is functional.
        '''
        self.new_user = User('Dennis', 'Mwaniki', 'Mwaniki91')
        self.new_user.save_user()
        user2 = User('Njoro', 'Mwamba', 'Kimani19')
        user2.save_user()
 
        for user in User.user_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user.first_name
        return current_user

        self.assertEqual(current_user, User.check_user(user2.password, user2.first_name))    
    
    

if __name__ == '__main__':
    unittest.main()