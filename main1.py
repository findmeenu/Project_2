import time
import os

def game_rules(): 
    
    print("WELCOME ! \n")
    print("PIG : DICE GAME \n" )
    print("The Game Rules: \n") 
    print("Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to \"hold\": \n" ) 
    print("-> If the player rolls a 1, they score nothing and it becomes the next player's turn.\n")
    print("->If the player rolls any other number, it is added to their turn total and the player's turn continues.\n")
    print("->If a player chooses to \"hold\", their turn total is added to their score, and it becomes the next player's turn. \n")
    print("The first player to score 100 or more points wins.")
    
    time.sleep(5)
    os.system("cls")

def main ():
    
    
    print("1. Play \n")
    print("2. Show History \n")
    print("3. Rules\n")
    print("4. Restart \n")
    print("5. Quit")
        
    choice = input("Enter the choice: ")
    
    while(choice != 5):
        if (choice == 1):
            print("1. Single player mode\n")
            print("2. Multiplayer mode\n")
            option = input("Enter your choice: ")
            if option == 1 :
                print("1. New Player")
                print("2. Existing Player")
                if option == 1:  #New Player
                    
                search_player(name)
                print("You would be facing Mr. Robot.")
                print("Select the difficulty level of Mr. Robot. ")
                print("1. EASY "
                      "2. NORMAL"
                      "3. HARD")
                difficulty_level_choice = input("Inter your choice: ")
            else:
                pass
        elif (choice == 2):
            pass
        elif(choice == 3):
            pass
        elif(choice == 4):
            pass 
        else:
            pass
            
            
            
    