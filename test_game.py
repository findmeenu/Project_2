from unittest.mock import MagicMock, patch
from io import StringIO
import unittest
import sys
import game
import random
#from unittest.mock import patch

class TestGameClass(unittest.TestCase):
    
    def setUp(self):
        self.gme = game.Game()
        # Create mock instances for p1_instance and p2_instance
        self.p1_instance_mock = MagicMock()
        self.p2_instance_mock = MagicMock()
        self.current_player_mock = self.p1_instance_mock
        self.p1_instance_mock.name = 'Player1'
        self.p2_instance_mock.name = 'Player2'
        self.dice_mock = MagicMock()
        
    def test_init_object(self):  
        # Checks the instance of game class & it's attributes value.
        self.assertIsInstance(self.gme, game.Game)
    
    def test_roll_first_heads(self):
        # Monkey patching to force random choice to be 'Heads'
        random.choice = lambda x: 'Heads'
        res = self.gme.roll_first("Bob", "Rock")
        self.assertEqual(res, "Bob")
        
    def test_roll_first_tails(self):
        # Monkey patching to force random choice to be 'Tails'
        random.choice = lambda x: 'Tails'
        res = self.gme.roll_first("Bob", "Rock")
        self.assertEqual(res, "Rock")
        
    def test_first_selects_player1(self):
        # Call the first_player method with "Player1" and the mock instances
        result = self.gme.first_player("Player1", self.p1_instance_mock, 
                                       self.p2_instance_mock)
    
    # Assert that the result returned by first_player is equal to p1_instance
        self.assertEqual(result, self.p1_instance_mock)

    def test_first_selects_player2(self):
        # Call the first_player method with "Player1" and the mock instances
        result = self.gme.first_player("Player2", self.p1_instance_mock, 
                                       self.p2_instance_mock)
    
    # Assert that the result returned by first_player is equal to p1_instance
        self.assertEqual(result, self.p2_instance_mock)
    
   
    def test_scoreboard_prints_correctly(self):
        # Set up the players score in mock instances.
        self.p1_instance_mock.score = 10
        self.p2_instance_mock.score = 45
        
        
        # Redirect stdout to capture printed output
        capturing_output = StringIO()
        sys.stdout = capturing_output
        
        self.gme.scoreboard(self.p1_instance_mock, self.p2_instance_mock)
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Get captured output
        printed_output = capturing_output.getvalue()
        
        # Assert that the output matches the expected format
        expected_output = "Player1 ----------------> 10\nPlayer2 ----------------> 45\n\n"
        self.assertEqual(printed_output, expected_output)

    
    def test_switch(self):
        # Call the first_player method with "Player1" and the mock instances
        result = self.gme.switch(self.current_player_mock, 
                        self.p1_instance_mock, self.p2_instance_mock)
    # Assert that the result returned by first_player is equal to p1_instance
        self.assertEqual(result, self.p2_instance_mock)

    def test_print_current_player1(self):
        # Redirect stdout to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.gme.print_current_player(self.current_player_mock)
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Get captured output
        printed_output = captured_output.getvalue()
        
        # Assert that the output matches the expected format
        expected_output = "Player1 turn now. Ready to Roll ! \n" +  "-" * 100 +"\n"
        self.assertEqual(printed_output, expected_output)


    @patch('sys.stdout', new_callable=StringIO)
    def test_roll_hold(self, mock_stdout):
        # Set up mock input    # Set up mock input
        mock_input = 'r'

        # Mock the roll method of the dice object
        self.dice_mock.roll.return_value = 5  # Mocking the roll method to return a fixed value

        # Call the roll_or_hold method
        result = self.gme.roll_or_hold(self.dice_mock, mock_input)

        # Check the return value
        self.assertEqual(result, 5)  # Assuming roll method returns 5

        # Check the printed output
        self.assertEqual(mock_stdout.getvalue(), '')  # No output should be printed

    def test_roll_hold2(self):        
        mock_input = 'h'
        # Call the roll_or_hold method
        result = self.gme.roll_or_hold(self.dice_mock, mock_input)
        # mock_input is hold then return value should be '0'
        # Check the return value
        self.assertEqual(result, 0)
        
        mock_input = 'q'
        # Call the roll_or_hold method
        result = self.gme.roll_or_hold(self.dice_mock, mock_input)
        # mock_input is hold then return value should be 2000
        # Check the return value
        self.assertEqual(result, 2000)
        
if __name__ == '__main__':
    unittest.main()
