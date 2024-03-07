#""Unit testing""

import unittest
import player


class TestPlayerClass(unittest.TestCase):
    
    def setUp(self):
        self.plyer = player.Player("Victory")
        
    def test_init_object(self):  #Checks the instance of player class & it's attributes value.
        self.assertIsInstance(self.plyer, player.Player)
        self.assertEqual(self.plyer.name, "Victory")
    
    def test__init__player__obj(self):   #Checks the instance of player class & it's attributes value.
        person_obj1 = player.Player("Ahmednuur")
        expected_name = person_obj1.name
        self.assertEqual(expected_name , "Ahmednuur")    
        
    def test_score1_rolled_6(self):   # Checks what happens when player rolls 6 and score earned so far by player is 10.
        self.plyer.score = 10
        self.plyer.score1(6)
        self.assertEqual(self.plyer.tempscore, 6)
        self.assertEqual(self.plyer.score, 10)
            
    def test_score1_rolled_2(self):      # Checks what happens when player rolls 6 & 2 and score earned so far by player is 70. As tempscore change not score.
        self.plyer.score = 70
        self.plyer.score1(6)
        self.plyer.score1(2)
        self.assertEqual(self.plyer.tempscore, 8)
        self.assertEqual(self.plyer.score, 84)
            
        
    def test_score1_rolled_1(self):  # Checks what happens when player rolls 1 and score earned so far by player is 50 & tempscore is 12.
        self.plyer.score = 50
        self.plyer.tempscore = 12
        self.plyer.score1(1)
        self.assertEqual(self.plyer.tempscore, 0)
        self.assertEqual(self.plyer.score, 50)
        
    def test_score1_rolled_0(self):      # Rolled 0 means player has opted for hold. Cheked here it's impact on tempscore and score.    
        self.plyer.score1(0)
        self.plyer.tempscore = 20
        self.assertEqual(self.plyer.tempscore, 20)
        self.assertEqual(self.plyer.score, 0)
        
    def test_score1_rolled_01(self):      # Rolled 0 means player has opted for hold. Cheked here it's impact on tempscore and score  
        self.plyer.score = 30
        self.plyer.tempscore = 5
        self.plyer.score1(0)
        self.assertEqual(self.plyer.tempscore, 0)
        self.assertEqual(self.plyer.score, 35)    
        
    def test_score1_rolled_100(self):      # Rolled 6 and cheked here it's impact on tempscore and score when score > 100
        self.plyer.score = 90
        self.plyer.tempscore = 5
        self.plyer.score1(6)        
       
        self.assertEqual(self.plyer.tempscore, 11)
        self.assertEqual(self.plyer.score, 101)  
        
    def test_score1_rolled_101(self):      #  Rolled 5 and cheked here it's impact on tempscore and score when score > 100   
        self.plyer.score = 90
        self.plyer.tempscore = 5
        self.plyer.score1(5)      
        self.assertEqual(self.plyer.tempscore, 10)
        self.assertEqual(self.plyer.score, 100)       #erroe
            
        
    def lost(self):                         # Checked the number of games won getting increased on every player win or not.
        self.plyer.loss = 4
        self.assertEqual(self.plyer.lost, 5)
        
    def test_update_score_1(self):
        person_obj2 = player.Player("Ahmednuur")
    
        person_obj2.score1(1)
        
        exp = person_obj2.score
        
        self.assertEqual(exp , 0)
        
    def test_update_score_anyothervalue (self):
        person_obj3 = player.Player("Ahmednuur")
        
        person_obj3.score1(5)
        
        exp = person_obj3.score
        
        self.assertEqual(exp , 0)
        
        
    def test_won_method(self):                              # Checking the count of games played & wins
        person_obj = player.Player("Meenu")
        
        expected_intial_winns = person_obj.wins
        
        expected_intital_gameplayed = person_obj.count_of_games_played
        
        person_obj.won()
        
        new_expected_wins = person_obj.wins
        new_expected_gameplayed = person_obj.count_of_games_played
        
        self.assertEqual(new_expected_wins , expected_intial_winns + 1)  
        self.assertEqual(new_expected_gameplayed , expected_intital_gameplayed + 1)
        
                
if __name__ == '__main__':
    unittest.main()
       