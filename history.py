
import player  # Make sure you have the 'player' module imported
import pickle

class History:
    
    def __init__(self):
        self.__player_data = {}
        self.__history = 'history_pig_game.pkl'  # Use .pkl extension for pickle files
        
    def save_players_dict(self):
        try:
            with open(self.__history, 'wb') as file:  # Open file in binary mode for pickle
                pickle.dump(self.__player_data, file)  # Dump the object to the file
            print("Player data saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving player data: {e}")

    def load_players_dict(self):
        try:
            with open(self.__history, 'rb') as file:  # Open file in binary mode for pickle
                self.__player_data = pickle.load(file)  # Load the object from the file
            print("Player data loaded successfully.")
        except FileNotFoundError:
            print(f"File '{self.__history}' not found.")
        except Exception as e:
            print(f"An error occurred while loading player data: {e}")


# ------------------------------------------------------            
    def addPlayer(self, player):
        if player.name in self.__player_data:
            self.__player_data[player.name].append((player.count_of_games_played, player.wins, player.loss))
        else:
            self.__player_data[player.name] = [(player.count_of_games_played, player.wins, player.loss)]

    def print_stats(self):
    # Print headers
        print("{:<20} {:<10} {:<10} {:<10}".format("Player Name", "Count", "Wins", "Losses"))
        print("-" * 60)  # Separator line
        
        # Print statistics for each player
        for player_name, game_stats in self.__player_data.items():
            for counts, wins, losses in game_stats:
                print("{:<20} {:<10} {:<10} {:<10}".format(player_name, counts, wins, losses))
        print("-" * 60)  # Separator line        
                        
    def stats_update_name_change(self, previous_name, changed_name):
        name_update = self.__player_data.pop(previous_name)
        self.__player_data[changed_name] = name_update
       
    # def print_stats(self):
    #     for player_name, game_stats in self.__player_data.items():
    #         print("Player Name:", player_name)
    #         for counts, wins, losses in game_stats:
    #             print("Count --------> ", counts)
    #             print("Wins----------> ", wins)
    #             print("Losses--------> ", losses)
