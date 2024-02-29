import player

# Contain a collection of player, prints its stats#

class Statistics: 

    def __init__(self):
        self.__player_data = {}
        self.__filename = "player_stats.bin" 
    
    

    def save_players_data (self, self.__filename):
        with open(filename, 'a+') as file :
            pickle.dump(self.__player_data, file)
    
    def load_players_list (self, self.__filename):
        with open(filename, 'rb') as file :
            self.__player_data = pickle.load(file)
            

    def addPlayer(self, player):
        if player.name in self.Player_data:
            self.__player_data[player.name].append((player.get_winns(), player.get_losses()))
        else:
            self.__player_data[player.name] = [(player.get_winns(), player.get_losses())]

    def print_stats(self):

        for player_name, game_stats in self.__player_data.items():
            print("Player Name:", player_name)
            for wins, losses in game_stats:
                print("Wins: ", wins)
                print("Losses: ", losses)


