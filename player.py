import pickle    
import sys 
import random

class Player :
    
    
   
    #write data to file & load it from file everytime"
    def __init__(self, name) :
        self.__name = name
        self.__players = []
        self.__score = 0
        #self.player_ID = self.generate_ID 
        #self.__playerID = playerID
        
    #pickle the list of players#
    
    def save_players_list (self, filename):
        with open(filename, 'a+') as file :
            pickle.dump(self.__players, file)
    
    def load_players_list (self, filename):
        with open(filename, 'rb') as file :
            self.__players = pickle.load(file)
            
        
        
        # To create new Player
        #no_of_players == len(players_dct)
        #players_dct [name] = (no_of_players + 1)
    
    def create_player (self, p_name):
        if p_name in self.__players :
            print ("Name already taken. Please select another name.")
            return False  # Indicate that name is already taken
        else:
            self.__players.append(p_name)
            print ("Player created.")
            return True   # Indicate that name is available & player created.
            
    def search_player (self, p_name):       
        if p_name in self.__players :
            return True  
        else:
            print("Please enter correct name.")
            return False   # Indicate that name is available # print("Enter correct name: ")
        
    
        #list_players['']
        #file 1 = sys.*args[1]
    
            
    def print_name(self):
        print (self.__name, self.__playerID)
        
    def change_name (self, orig_name, new_name):
        if orig_name in self.__players and new_name not in self.__players:
            self.__players.remove (orig_name)
            self.__players.append (new_name)
            print ("Name changed successfully.")
        elif orig_name in self.__players and new_name in self.__players:
            print ("Name already taken. Please select another name.")   
        else:
            print("Name does not exist. Select option 'Create New Player'.")
            
            
    def play (self, ):
        
        pass
        
        
    def score (self, roll_dice_num):
        total=0
        if roll_dice_num !=1: 
            total += roll_dice_num
            self.score += total
            return self.score
        else :
            return self.score
        
        
    def __str__(self):
        return f'The Player Name is {self.__name}, {self.__playerID}, {self.__score}'    