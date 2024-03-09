import pickle

class History:
    
    def __init__(self):
        self.__player_data = {}
        self.__history = 'history_pig_game1.pkl'  # Use .pkl extension for pickle files
        
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

    def addPlayer(self, player):
        player.name = player.name.lower()
        if player.name in self.__player_data:
            list_old_data = self.__player_data[player.name] 
            # If the player already exists in the dictionary, update their data
            list_old_data[0] += player.count_of_games_played
            list_old_data[1] += player.wins
            list_old_data[2] += player.loss
            self.__player_data[player.name] = list_old_data
        else:
            # If the player is new, create a new entry with their data
            self.__player_data[player.name] = [player.count_of_games_played, player.wins, player.loss]

                
    def print_stats(self):
         # Print headers
        print("{:<20} {:<10} {:<10} {:<10}".format("Player Name", "Count", "Wins", "Losses"))
        print("-" * 60)  # Separator line
        
        # Print statistics for each player
        for player_name, game_stats in self.__player_data.items():
            print("{:<20} {:<10} {:<10} {:<10}".format(player_name, *game_stats))
        print("-" * 60)  # Separator line        
                        
    def stats_update_name_change(self, previous_name, changed_name):
        previous_name = previous_name.lower()
        changed_name = changed_name.lower()
        name_update = self.__player_data.pop(previous_name)
        self.__player_data[changed_name] = name_update
