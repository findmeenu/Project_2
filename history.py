import pickle
import player  # Make sure you have the 'player' module imported

class History:
    def __init__(self):
        self.__player_data = {}
        self.__filename = "player_stats.bin"

    def save_players_data(self):
        with open(self.__filename, 'wb') as file:  # Use 'wb' for writing in binary mode
            pickle.dump(self.__player_data, file)

    def load_players_list(self):
        with open(self.__filename, 'rb') as file:  # Use 'rb' for reading in binary mode
            return self.__player_data == pickle.load(file)


def create_player (self, p_name):
        if p_name in self.__players :
            print ("Name already taken. Please select another name.")
            return True  # Indicate that name is already taken
        else:
            self.__players.append(p_name)
            print ("Player created.")
            return False   # Indicate that name is available & player created.
            
    def search_player(self, p_name):       
        if p_name not in self.__players :
            print("Please enter correct name.")
            return True  
        else:
            return False   # Indicate that name is available # print("Enter correct name: ")
        
    def addPlayer(self, player):
        if player.name in self.__player_data:
            self.__player_data[player.name].append((player.get_winns(), player.get_losses()))
        else:
            self.__player_data[player.name] = [(player.get_winns(), player.get_losses())]

    def print_stats(self, statistics.load_players_list()):

        for player_name, game_stats in self.__player_data.items():
            print("Player Name:", player_name)
            for wins, losses in game_stats:
                print("Wins: ", wins)
                print("Losses: ", losses)


  

