import random
import unittest
from unittest.mock import MagicMock, patch
import computer
import dice


class TestComputerClass(unittest.TestCase):
    
    def setUp(self):
        self.comp = computer.Computer('Mr. Z')
        self.die = dice.Dice()
                
    def test_init_object(self):
        # Checks the instance of computer class.
        self.assertIsInstance(self.comp, computer.Computer)
        
    def test_score1_rolled_6(self):   # Checks what happens when computer rolls 6 and score earned so far by player is 10.
        self.comp.score = 10
        self.comp.score1(6)
        self.assertEqual(self.comp.tempscore, 6)
        self.assertEqual(self.comp.score, 10)
            
    def test_score1_rolled_2(self):      # Checks what happens when computer rolls 6 & 2 and score earned so far by player is 70. As tempscore change not score.
        self.comp.score = 70
        self.comp.score1(6)
        self.comp.score1(2)
        self.assertEqual(self.comp.tempscore, 8)
        self.assertEqual(self.comp.score, 70)
            
        
    def test_score1_rolled_1(self):  # Checks what happens when computer rolls 1 and score earned so far by player is 50 & tempscore is 12.
        self.comp.score = 50
        self.comp.tempscore = 12
        self.comp.score1(1)
        self.assertEqual(self.comp.tempscore, 0)
        self.assertEqual(self.comp.score, 50)
        
    def test_score1_rolled_0(self):      # Rolled 0 means computer has opted for hold. Cheked here it's impact on tempscore and score.    
        self.comp.score1(0)
        self.comp.tempscore = 20
        self.assertEqual(self.comp.tempscore, 20)
        self.assertEqual(self.comp.score, 0)
        
    def test_score1_rolled_100(self):      # Rolled 2 and cheked here it's impact on tempscore and score when score = 100
        self.comp.score = 94
        self.comp.tempscore = 4
        self.comp.score1(2)
        self.assertEqual(self.comp.tempscore, 6)
        self.assertEqual(self.comp.score, 100)    
        
    def test_score1_rolled_101(self):      # Rolled 5 and cheked here it's impact on tempscore and score when score > 100
        self.comp.score = 90
        self.comp.tempscore = 5
        self.comp.score1(6)        
       
        self.assertEqual(self.comp.tempscore, 11)
        self.assertEqual(self.comp.score, 101)  
        
    def test_score1_rolled_95(self):      #  Rolled 4 & 1 and cheked here it's impact on tempscore and score when score < 100   
        self.comp.score = 95
        self.comp.score1(4)
        self.comp.score1(1)      
        self.assertEqual(self.comp.tempscore, 0)
        self.assertEqual(self.comp.score, 95)
            
    # def test_strategy(self):
    #     difficulty_level = 1
    #     res = self.comp.strategy(difficulty_level)
    #     self.assertEqual(res, 'a') 
       
    @patch.object(random, 'randint', return_value=1)  # Patch the randint function
    def test_strategy_easy1(self, mock_randint):
        self.comp.tempscore = 5 # Set tempscore to a value less than or equal to 10
        option = self.comp.easy()
        self.assertEqual(option, 'r')  # Assert that 'r' is returned
        #mock_randint.assert_called_once_with(1, 3)  # Assert that randint was called with arguments (1, 3)

    @patch.object(random, 'randint', return_value=2)  # Patch the randint function
    def test_strategy_easy2(self, mock_randint):
        self.comp.tempscore = 5 # Set tempscore to a value less than or equal to 10
        option = self.comp.easy()
        self.assertIn(option, ['r', 'h'])  # Option should be either 'r' or 'h'

    @patch.object(random, 'randint', return_value=3)  # Patch the randint function
    def test_strategy_easy3(self, mock_randint):
        self.comp.tempscore = 5 # Set tempscore to a value less than or equal to 10
        option = self.comp.easy()
        self.assertIn(option, ['r', 'h'])  # Option should be either 'r' or 'h'

    @patch.object(random, 'randint', return_value=1)  # Patch the randint function
    def test_strategy_normal1(self, mock_randint):
        self.comp.tempscore = 15 # Set tempscore to a value less than or equal to 10
        option = self.comp.normal()
        self.assertEqual(option, 'h')  # Option should be 'h'
    
    @patch.object(random, 'randint', return_value=2)  # Patch the randint function
    def test_strategy_normal2(self, mock_randint):
        self.comp.tempscore = 20     # Set tempscore to a value less than or equal to 10
        option = self.comp.normal()
        self.assertEqual(option, 'h')  # Option should be  'r'
        
    @patch.object(random, 'randint', return_value=3)  # Patch the randint function
    def test_strategy_normal3(self, mock_randint):
        self.comp.tempscore = 50 # Set tempscore to a value less than or equal to 10
        option = self.comp.normal()
        self.assertIn(option, ['r', 'h'])  # Option should be either 'r' or 'h'

    def test_hold_or_roll_comp1(self):
        # Define a mock value for the strategy method
        self.comp.strategy = MagicMock(return_value='r')
         # Define a mock value for the roll method of the die instance
        self.die.roll = MagicMock(return_value=4) 
        # Call the hold_or_roll_comp method with the mock die instance and difficulty level
        
        result = self.comp.hold_or_roll_comp(self.die, 1)
        
        # Assert that the value returned by hold_or_roll_comp is equal to the value returned by die.roll
        self.assertEqual(result, 4)
    
    def test_hold_or_roll_comp2(self):
        # Define a mock value for the strategy method
        self.comp.strategy = MagicMock(return_value='h')
        
        # Call the hold_or_roll_comp method with the mock die instance and difficulty level
        
        result = self.comp.hold_or_roll_comp(self.die, 1)
        
        # Assert that the value returned by hold_or_roll_comp is equal to the value = 0
        self.assertEqual(result, 0)    
                
if __name__ == '__main__':
    unittest.main()
                   