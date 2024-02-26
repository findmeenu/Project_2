import pickle    
import sys 
import random

class Player :
    
    
   
    #write data to file & load it from file everytime"
    def __init__(self, name) :
        self.__name = name
        self.__players = []
        #self.player_ID = self.generate_ID 
        #self.__playerID = playerID
        
    #pickle the list of players#
    
    def save_players_list ():
        with open('players.pkl', 'a+') as file :
            pickle.dump(players, file)
    
    def load_players_list ():
        with open('players.pkl', 'rb') as file :
            players = pickle.load(file)
            
    #def create_new_player (p_name): 
        
    #    return random.randint(1000 , 9999)
        
        
        # To create new Player
        #no_of_players == len(players_dct)
        #players_dct [name] = (no_of_players + 1)
        
            
    def search_player (self, p_name):       
        if p_name in self.__players :
            print ("Name already taken. Please select another name.")
            return False  # Indicate that name is already taken
        else:
            self.__players.append(p_name)
            return True   # Indicate that name is available
        
    
        #list_players['']
        #file 1 = sys.*args[1]
            
    def print_name(self):
        print (self.__name, self.__playerID)
        
    def change_name (self):
        pass
        
    def roll_dice (self):
        pass
        
    def set_score (self):
        pass
        
    def __str__(self):
        return f'The Player Name is {self.__name}, {self.__playerID}'    