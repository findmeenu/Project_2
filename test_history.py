import unittest
import os
import pickle
from unittest.mock import patch
from history import History
from player import Player

class TestHistory(unittest.TestCase):

    def setUp(self):
        self.hist = history.History()
        self.hist.player_data  = {
            'alice': [5, 3, 2],
            'bob': [8, 5, 3]
        }
        self.hist.history = 'history_test.pkl'
        
    def tearDown(self):
        if os.path.exists(self.hist.history):
            os.remove(self.hist.history)

    # def test_save_players_dict(self):
    #     self.hist._History__player_data = self.test_players
    #     self.test_history.save_players_dict()
    #     self.assertTrue(os.path.exists(self.test_history._History__history))

    # def test_load_players_dict(self):
    #     with open(self.test_history._History__history, 'wb') as file:
    #         pickle.dump(self.test_players, file)
    #     self.test_history.load_players_dict()
    #     self.assertEqual(self.test_history._History__player_data, self.test_players)

    # def test_addPlayer(self):
    #     player1 = Player('Alice', 2, 1, 1)
    #     player2 = Player('Bob', 3, 2, 1)
    #     self.test_history.addPlayer(player1)
    #     self.test_history.addPlayer(player2)
    #     expected_data = {
    #         'alice': [7, 4, 3],
    #         'bob': [11, 7, 4]
    #     }
    #     self.assertEqual(self.test_history._History__player_data, expected_data)

    # def test_print_stats(self):
    #     with patch('builtins.print') as mocked_print:
    #         self.test_history._History__player_data = self.test_players
    #         self.test_history.print_stats()
    #         mocked_print.assert_called_with("{:<20} {:<10} {:<10} {:<10}".format("Player Name", "Count", "Wins", "Losses"))

    # def test_stats_update_name_change(self):
    #     self.test_history._History__player_data = self.test_players
    #     self.test_history.stats_update_name_change('Alice', 'Alicia')
    #     expected_data = {
    #         'alicia': [5, 3, 2],
    #         'bob': [8, 5, 3]
    #     }
    #     self.assertEqual(self.test_history._History__player_data, expected_data)

if __name__ == '__main__':
    unittest.main()
