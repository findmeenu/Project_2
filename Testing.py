import player 

def Testing():
    d = []
    print(len(d))
    p_name = input("Enter your name: ")
#b = player.Player1(pla) 


#player1_instance = create_player(Player1, a)
    search_player(p_name)
    print(len(d))

def search_player (p_name):       
        if p_name in d :
            print ("Name already taken. Please select another name.")
            return False  # Indicate that name is already taken
        else:
            players.append(p_name)
            
            return True   # Indicate that name is available
        
        
        
if __name__ == "__Testing__":
    Testing() 
