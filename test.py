import pyperclip
import unittest # Importing the unittest module
from user import User,Credentials # Importing the contact class

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

class TestCredentials(unittest.TestCase):
    '''
    Defines test cases for the credentials class behaviours.
    '''    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''

        self.new_credential = Credentials("Dennis", "Instagram", "dennism", "nakuru@91")
    
    def test__init__(self):
        '''
        test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_credential.user_name, "Dennis")
        self.assertEqual(self.new_credential.site_name, "Instagram")
        self.assertEqual(self.new_credential.account_name, "dennism")
        self.assertEqual(self.new_credential.password, "nakuru@91")  

    def tearDown(self):
        '''
        Clears the credentials list.
        '''
        Credentials.credentials_list = []

    def test_save_credentials(self):
        '''
        Testing if credentials are saved in credentials list.
        '''
        self.new_credential.save_credential()
        twitter = Credentials("Dennis", "Twitter", "dennism", "nakuru@91")
        twitter.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 2)
    
    def test_display_credentials(self):
        '''
        Test case to test if our objects show.
        '''
        self.new_credential.save_credential()
        twitter = Credentials("Dennis", "Twitter", "dennism", "nakuru@91")
        twitter.save_credential()
        gmail = Credentials('fennis','Gmail','mephism','naks222')
        gmail.save_credential()
        self.assertEqual(len(Credentials.display_credentials(twitter.user_name)), 2)

    def test_del_credential(self):
        '''
        Test if we can delete a saved credential.
        '''
        self.new_credential.save_credential()
        new_credential = Credentials('fennis','Gmail','mephism','naks222')
        new_credential.save_credential()

        self.new_credential.del_credential()
        self.assertEqual(len(Credentials.credentials_list), 1)  
    
    def test_credential_exists(self):
        '''
        Test  to check if a credential exists in the credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials('fennis','Gmail','mephism','naks222')
        test_credential.save_credential()
        credential_exists = Credentials.credential_exist("Gmail")
        self.assertTrue(credential_exists)

    def test_find_by_site_name(self):
        '''
        search credential by site_name and return the right details.
        '''
        self.new_credential.save_credential()
        gmail = Credentials('fennis','Gmail','mephism','naks222')
        gmail.save_credential()
        credential_exists = Credentials.find_by_site_name('Gmail')
        self.assertEqual(credential_exists, gmail)


    def test_copy_credential(self):
        '''
        Test if the copy credential method copies the correct credential from credit list.
        '''
        self.new_credential.save_credential()
        twitter = Credentials("Dennis", "Twitter", "dennism", "nakuru@91")
        twitter.save_credential()
        find_credential = None
        for credential in Credentials.users_credentials_list:
            find_credential = Credentials.find_by_site_name(credential.site_name)
            return pyperclip.copy(find_credential.password)
        Credentials.copy_credential(self.new_credential.site_name)
        self.assertEqual('nakuru@91', pyperclip.paste())
        print(pyperclip.paste())



if __name__ == '__main__':
    unittest.main()