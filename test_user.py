import sys
from io import StringIO
import unittest
import user
import os

class TestUserClass(unittest.TestCase):
    
    def setUp(self):
         # Create a test instance of the User class
        self.use = user.User()
        self.use.filename = 'test_users.txt'
        # Define test data
        self.use.players = ['alice', 'bob', 'charlie']

    def tearDown(self):
        # Clean up by removing the test file if it was created during the tests
        if os.path.exists(self.use.filename):
            os.remove(self.use.filename)
            
    def test_save_players_list(self):
        # "# Add some players to the test instance"
        # self.use.players = ['Alice', 'Bob', 'Charlie']

        # Call the save_players_list method
        self.use.save_players_list()

        # Check if the file was created and contains the expected content
        self.assertTrue(os.path.exists(self.use.filename))  # Check if the file exists
        with open(self.use.filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, 'alice\nbob\ncharlie\n')  # Check if file content matches expected content

    def test_load_players_list(self):
        # Create a test file with player names
        with open(self.use.filename, 'w') as file:
            file.write('dave\neva\nfrank\n')

        # Call the load_players_list method
        self.use.load_players_list()

        # Check if the players list was loaded correctly
        expected_players = ['dave', 'eva', 'frank']
        self.assertEqual(self.use.players, expected_players)  # Check if the loaded players list matches expected
                
    def test_init_object(self):  #Checks the instance of user class & it's attributes value.
        self.assertIsInstance(self.use, user.User)
        
    
    def test_create_player(self):
        # Test creating a new player
        res = self.use.create_player('BOB')
        self.assertEqual(res, '1')  # Expect '1' to indicate name already taken
        res = self.use.create_player('Rock')
        # Test creating a player with an existing name
        self.assertEqual(res, 'rock')  # Expect player name to be returned 
                                        # in lower case if player does not exist.

    def test_search_player(self):
        # Test search an existing new player in the players list.
        res = self.use.search_player('BOB')
        self.assertEqual(res, 'bob')  # Expect player name to be returned 
                                        # in lower case if player exist.

        res = self.use.search_player('Rock')
        # Test search a player with an existing name
        self.assertEqual(res, '1')  # Expect '1' if name is not in existing users list.

#         # Load test players into the user instance
#         self.test_user.players = self.test_players
        


    def test_change_name1(self):
        # Redirect stdout to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.assertIn('bob', self.use.players)  # Expect 'bob' to be in players list
        self.assertNotIn('Bobby', self.use.players)  # Expect 'bobby' not to be in players list
        self.use.change_name('bob', 'Bobby')
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Get captured output
        printed_output = captured_output.getvalue()
        
        # Test changing name successfully
        self.assertEqual(printed_output, "Name changed successfully.\n")
        
    def test_change_name2(self):
        # Redirect stdout to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.assertIn('alice', self.use.players)  # Expect 'alice' to be in players list
        self.assertIn('charlie', self.use.players)  # Expect 'charlie' to be in players list
        self.use.change_name('alice', 'charlie')
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Get captured output
        printed_output = captured_output.getvalue()
        
        # Test changing name successfully
        self.assertEqual(printed_output, "Name already taken. Please select another name.\n")
        
    def test_change_name3(self):
        # Redirect stdout to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.assertNotIn('cat', self.use.players)  # Expect 'cat' to be in players list
        self.assertNotIn('dog', self.use.players)  # Expect 'dog' not to be in players list
        self.use.change_name('cat', 'dog')
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Get captured output
        printed_output = captured_output.getvalue()
        
        # Test if name is not in existing player list.
        self.assertEqual(printed_output, "Name does not exist. Select option 'Create New Player'.\n")        
        
if __name__ == '__main__':
    unittest.main()
