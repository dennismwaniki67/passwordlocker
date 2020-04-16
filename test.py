import unittest # Importing the unittest module
from user import User # Importing the contact class

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
        User.users_list = []    

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)
    
    

if __name__ == '__main__':
    unittest.main()