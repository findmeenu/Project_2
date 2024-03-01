import time
import os
import player

def main1():
#___________________________________________________________MAIN MENU_______________________________________________________________     
   
    keep_running = True  # To start the main menu.
    while keep_running:
        main_menu()     
        choice = int(input("Enter the choice (1-5): "))
        
#____________________________________MAIN MENU - BAD INPUT Check _______________________________________________________________________________
        
        if 1 <= choice <=5 :
            print ("Invalid input. Please enter a number (1-5).")
            keep_running = True  
#____________________________________MAIN MENU SELECTED : 1. PLAY_________________________________________________________________               
#  ------------------------------- # To start sub menu single or multiplayer mode.-------------------------------------------------------      
        elif choice == 1:                                   
            play = True
            
            while play:
                print("1. Single player mode")
                print("2. Multiplayer mode")
                print("3. Main Menu")
                print()
                option_1 = int(input("Enter your choice (1-3): "))
 # ------------------------------- # To check bad data for sub menu single or multiplayer mode.-------------------------------------------------------      
 #---------------------------------------------------------------------------------------------------------------------------       
                     
                if 1 <= option_1 <=3:
                    print ("Invalid input. Please enter a number (1-3).")
                    play = True
 #  ------------------------------- # To start sub menu single mode.-------------------------------------------------------      
 #---------------------------------------------------------------------------------------------------------------------------       
                      
                elif option_1 == 1 :                                #Single player mode ON
                    if sub_menu_1_execute() == 'Start':
                        print ("Let's the Fun Begin ! ")
                        game.start.game()
                    else:
                        play = True    
                           
##---------------------------------- # sub menu - If multiplayer mode is selected.-------------------------------------------------------      
##-------------------------------------------------------------------------------------------------------------------------------------                            
                
                elif option_1 == 2 :                    # Multiplayer mode ON
                    print(" ENTER DATA FOR PLAYER 1.")
                    player_1 = sub_menu_1_execute() 
                    
                    print ("ENTER DATA FOR PLAYER 2")
                    player_2 = sub_menu_1_execute()
                    
                    if player_1 and player_2 == 'Start':
                        print ("Let's the Fun Begin ! ")
                        pass # create 2 instances for both player to start the game.
                            
                    else:
                        play = True
##---------------------------------- # sub menu - If Go back mode is selected.-------------------------------------------------------      
##-------------------------------------------------------------------------------------------------------------------------------------                            
                        
                elif option_1 == 3:
                    play = False
                    keep_running = True     
##---------------------------------- # Exit Sub menu-------------------------------------------------------------------------------------      
#____________________________________MAIN MENU SELECTED : 2. SHOW HISTORY _________________________________________________________________               


        elif choice == 2:
            pass
#____________________________________MAIN MENU SELECTED : 3. RULES _________________________________________________________________               

        elif choice == 3:
            game_rules ()
#___________________________________MAIN MENU SELECTED : 4. RESTART _________________________________________________________________               

        elif choice == 4:
            pass

#____________________________________MAIN MENU SELECTED : 5. QUIT _________________________________________________________________               
        elif choice == 5:
            keep_running = False
        
           
            
def game_rules(): 
    
    print("WELCOME ! \n")
    print("PIG : DICE GAME \n" )
    print("The Game Rules: \n") 
    print("Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to \"hold\": \n" ) 
    print("-> If the player rolls a 1, they score nothing and it becomes the next player's turn.")
    print("-> If the player rolls any other number, it is added to their turn total and the player's turn continues.")
    print("-> If a player chooses to \"hold\", their turn total is added to their score, and it becomes the next player's turn. \n")
    print("The first player to score 100 or more points wins.")
    
    time.sleep(5)
    os.system("cls")

def main_menu():
                
    print("1. Play")
    print("2. Show History")
    print("3. Rules")
    print("4. Restart")
    print("5. Quit")
    print()        
    
    
def sub_menu_1():
    print("1. New Player")
    print("2. Existing Player")
    print("3. Go Back")
    print()
    
    
def sub_menu_1_execute():
    new_or_existing_player = True
    while new_or_existing_player :
        sub_menu_1()                                    # New or existing player ?
        option_2 = int(input("Enter your choice (1-3): "))
        
        if 1 <= option_2 <=2:
            new_or_existing_player = True     
                            
        elif option_2 == 1:
            new_player = True
            while new_player:
                new_name = input ("Enter name to create Player: ")                   #New Player
                if player.create_player(new_name):
                    new_player = True
                else :
                    new_player = False
                    return 'Start'
#create player instance and start playing the game. 

        elif option_2 == 2:
            existing_player = True
            while existing_player :
                old_name = input("Provide Player Name: ")                   #Exisiting player
                if player.search_player (old_name) :
                    existing_player = True
                else:
                    existing_player = False
                    return 'Start'

#create player instance and start playing the game. 
        elif option_2 == 3:
            new_or_existing_player == False
            return 'Go Back'
        
                