import pickle 
   

class User:
        # write data to file & load it from file everytime"
    def __init__(self, name):
        self.__name = name
        self.__players = []
        self.__score = 0
        self.__filename = 'players.bin'
    
    def save_players_list(self):
        with open(self.__filename, 'a+b') as file: 
            pickle.dump(self.__players, file)

    def load_players_list(self):
        with open(self.__filename, 'rb') as file:  
            self.__players == pickle.load(file)

    def create_player(self, p_name):
        if p_name in self.__players:
            print("Name already taken. Please select another name.")
            return True  # Indicate that name is already taken
        else:
            self.__players.append(p_name)
            print("Player created.")
            return False   # Indicate that name is available & player created.
            
    def search_player(self, p_name):       
        if p_name not in self.__players:
            print("Please enter correct name.")
            return True  
        else:
            return False      # Indicate that name is available # print("Enter correct name: ")             
        
    def change_name(self, orig_name, new_name):
        if orig_name in self.__players and new_name not in self.__players:
            self.__players.remove(orig_name)
            self.__players.append(new_name)
            print("Name changed successfully.")
        elif orig_name in self.__players and new_name in self.__players:
            print("Name already taken. Please select another name.")
        else:
            print("Name does not exist. Select option 'Create New Player'.")
