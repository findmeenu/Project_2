
import game
import player
import dice
import history

def main1():
    player.load_players_list()
    my_dice = dice.Dice()
    pig_game = game.Game()
    
    pig_game.game_rules()
#___________________________________________________________MAIN MENU_______________________________________________________________     
    
    keep_running = True  # To start the main menu.
    while keep_running:
        main_menu()     
        choice = int(input("Enter the choice (1-5): "))
        
#____________________________________MAIN MENU - BAD INPUT Check _______________________________________________________________________________
        
        if 1 < choice < 6 :
            print ("Invalid input. Please enter a number (1-5).")
             
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
                     
                if 1 < option_1 < 3:   # bad data check
                    print ("Invalid input. Please enter a number (1-3).")
                    
 #  ------------------------------- # To start sub menu single mode.-------------------------------------------------------      
 #---------------------------------------------------------------------------------------------------------------------------       
                      
                elif option_1 == 1 :                                #Single player mode ON
                    a,b = sub_menu_1_execute()
                    if  b == 'Start':
                        
                        level = True
                        while level:
                            print("You would be facing Mr. Robot.")
                            print("Select the difficulty level of Mr. Robot. ")
                            print("1. EASY /n2. NORMAL/n3. HARD")
                            difficulty_level = int(input("Enter your choice: "))
                            if 1 < difficulty_level < 3:
                                print("Invalid input. Please enter a number (1-3).")
                            elif difficulty_level == 1:
                                level = False
                                print("Let's begin Fun!")    
##missing mistery
                        
                        #game start 
                        p1 = player.Player(a)
                        mr_robot = computer.Computer()
                        
                        z = pig_game.roll_first(p1, mr_robot)
                        
                        p1.set
                        if z == p1:
                            num = my_dice.roll()
                            total score for p1 = p1.score(num)
                            #write from here.
                            p1.roll_
                        my_player.play
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
                        
##---------------------------------- # Exit Sub menu-------------------------------------------------------------------------------------      
#____________________________________MAIN MENU SELECTED : 2. SHOW HISTORY _________________________________________________________________               


        elif choice == 2:
            
            statistics.print_stats(statistics.load_players_list())
            
#____________________________________MAIN MENU SELECTED : 3. RULES _________________________________________________________________               

        elif choice == 3:
            pig_game.game_rules ()
           
#___________________________________MAIN MENU SELECTED : 4. RESTART _________________________________________________________________               

        elif choice == 4:
            pass
#____________________________________MAIN MENU SELECTED : 5. CHANGE NAME _________________________________________________________________               

        elif choice == 5:
            existing_name = input("Enter exisitng name: ")
            change_name = input("Enter the desired name: ")
            
            my_player.change_name(existing_name, change_name)
            choice == 5
        
#____________________________________MAIN MENU SELECTED : 6. QUIT _________________________________________________________________               
        elif choice == 6:
            my_player.save_players_list()
            
            keep_running = False
        
if __name__ == "__main1__":
    main()           
            

def main_menu():
    print("-------Dice Game--------")            
    print("1. Play")
    print("2. Show History")
    print("3. Rules")
    print("4. Restart")    
    print("5. Change Name")
    print("6. Quit")
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
        
        if 1 < option_2 <3:
            print ("Invalid input. Please enter a number (1-3).")     
                            
        elif option_2 == 1:
            new_player = True
            while new_player:
                new_name = input ("Enter name to create Player: ")                   #New Player
                if my_player.create_player(new_name):
                    new_player = True
                else :
                    new_player = False
                    return new_player, 'Start'
#create player instance and start playing the game. 

        elif option_2 == 2:
            existing_player = True
            while existing_player :
                old_name = input("Provide Player Name: ")                   #Exisiting player
                if my_player.search_player(old_name) :
                    existing_player = True
                else:
                    existing_player = False
                    return old_name, 'Start'

#create player instance and start playing the game. 
        elif option_2 == 3:
            new_or_existing_player == False
            return 'Go Back'
        
                