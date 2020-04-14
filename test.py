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
        self.new_contact = User("Dennis","Mwaniki","Mwaniki91") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.first_name,"Dennis")
        self.assertEqual(self.new_contact.last_name,"Mwaniki")
        self.assertEqual(self.new_contact.password,"Mwaniki91")


if __name__ == '__main__':
    unittest.main()