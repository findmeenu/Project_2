import display
import user
import game
import player
import dice
import history
import computer

def main():
    my_player = user.User()
    my_history = history.History()
    pig_game = game.Game()
    my_dice = dice.Dice()
    my_player.load_players_list()
    my_history.load_players_dict()
    display.game_rules()
#___________________________________________________________MAIN MENU_______________________________________________________________     
    
    keep_running = True  # To start the main menu.
    while keep_running:
        display.main_menu()     
        choice = input("Enter the choice (1-6): ")
        
#____________________________________MAIN MENU - BAD INPUT Check _____________________________________________________________________________      
        if choice < "1" or choice > "6":
            print("Invalid input. Please enter a number (1-6).")
             
#____________________________________MAIN MENU SELECTED : 1. PLAY_________________________________________________________________               
#  ------------------------------- # To start sub menu single or multiplayer mode.-------------------------------------------------------      
        elif choice == "1":                                   
            play = True
            
            while play:
                display.single_or_multi() #Print menu single/Multiplayer/Main Menu
                option_1 = input("Enter your choice (1-3): ")
 # ------------------------------- # To check bad data for sub menu single or multiplayer mode.-------------------------------------------------------      
 #---------------------------------------------------------------------------------------------------------------------------       
                     
                if option_1 < "1" or option_1 > "3":   # bad data check
                    print("Invalid input. Please enter a number (1-3).")
                    
 #  ------------------------------- # To start sub menu single mode.-------------------------------------------------------      
 #---------------------------------------------------------------------------------------------------------------------------       
                      
                elif option_1 == "1":  #Single player mode ON
                    print("-> ENTER DATA FOR PLAYER 1.\n")
                
                    player_1, b = sub_menu_1_execute(my_player) 
                    player_2 = "Mr. Robot"
                    
                    play = False
                    level = True
                    
                    while level:
                        display.robot_level()
                        difficulty_level = input("Enter your choice: ")
                
                        if difficulty_level < "1" or difficulty_level > "2":  #Bad data input
                            print("Invalid input. Please enter a number (1-2).")
                        
                        elif difficulty_level == "1" or difficulty_level == "2":
                            level = False
                ##########################################################
            
                    if b == 'Start' and (difficulty_level == "1" or difficulty_level == "2"):
    
                        display.start_game()            #Print let's begin fun
                        p1_instance = player.Player(player_1)
                        p2_instance = computer.Computer(player_2)
                        
                        #z = player.Player(meenu)
                        player_name = pig_game.roll_first(player_1, player_2)
                        current_player = pig_game.first_player(
                            player_name, p1_instance, p2_instance)
                        
                        start_playing = True
                        while start_playing:
                            if current_player == p1_instance:
                                value = hold_or_roll(my_dice, pig_game)
                                
                            elif current_player == p2_instance:
                               
                                print("11111111111-----cut no roll here")
                               
                                #current_player.score1(value)
                                value = p2_instance.hold_or_roll_comp(
                                        my_dice, difficulty_level)    
                                print("2222222222222222222")
                                print(value)
                            current_player.score1(value)
                            
                            print("-------------------------------Score----------------")
                            if value == 1: #Switch because of dice rolled 1
                                play_logic(pig_game, current_player, p1_instance, p2_instance)
                                
                                        
                            elif value == 0:   #Switch because of user selected to hold
                                play_logic(pig_game, current_player, p1_instance, p2_instance)
                            
                            elif value == 2000:  # When player want to restart & press 'Q/q'
                                start_playing = False
                                play = True    
                                    
                            else: #When either of the player has reached roll value 100
                                if p1_instance.score > 30:
                                    print(f"{p1_instance.name} is the WINNER !.")
                                    p1_instance.won()
                                    my_history.addPlayer(p1_instance)
                                    print()
                                    start_playing = False
                                    play = True
                                    
                                elif p2_instance.score > 30:
                                    
                                    print(f"{p2_instance.name} is the WINNER !.")
                                    p1_instance.lost()
                                    my_history.addPlayer(p1_instance)
                                    print()
                                    start_playing = False
                                    play = True
                                    
                    
                           
##---------------------------------- # sub menu - If multiplayer mode is selected.-------------------------------------------------------      
##-------------------------------------------------------------------------------------------------------------------------------------                            
                
                elif option_1 == "2":         # Multiplayer mode ON
                    print("\n-> ENTER DATA FOR PLAYER 1.\n")
                    player_1, x = sub_menu_1_execute(my_player) 
                    
                    print("\n-> ENTER DATA FOR PLAYER 2\n")
                    player_2, y = sub_menu_1_execute(my_player)
                    
                    play = False
                    
                    if x == 'Start' and y == 'Start':
                        display.start_game()            #Print let's begin fun
                        p1_instance = player.Player(player_1)
                        p2_instance = player.Player(player_2)
                        
                        player_name = pig_game.roll_first(player_1, player_2)
                        current_player = pig_game.first_player(
                            player_name, p1_instance, p2_instance)
                        
                        start_playing = True
                        while start_playing:
                            
                            value = hold_or_roll(my_dice, pig_game)
                            current_player.score1(value)
                            
                            print("-------------------------------Score----------------")
                            if value == 1: # Switch because of dice rolled 1
                                play_logic(pig_game, current_player, p1_instance, p2_instance)
                                        
                            elif value == 0:   #Switch because of user selected to hold
                            
                                play_logic(pig_game, current_player, p1_instance, p2_instance)
                            
                            elif value == 2000:  # When player want to restart & press 'Q/q'
                                start_playing = False
                                play = True    
                                    
                            else: #When either of the player has reached roll value 100
                                if p1_instance.score > 30:
                                    print(f"{p1_instance.name} is the WINNER !.")
                                    p1_instance.won()
                                    p2_instance.lost()
                                    my_history.addPlayer(p1_instance)
                                    my_history.addPlayer(p2_instance) 
                                    print()
                                    start_playing = False
                                    play = True
                                    
                                elif p2_instance.score > 30:
                                    
                                    print(f"{p2_instance.name} is the WINNER !.")
                                    p1_instance.lost()
                                    p2_instance.won()
                                    my_history.addPlayer(p1_instance)
                                    my_history.addPlayer(p2_instance) 
                                    print()
                                    start_playing = False
                                    play = True
                    
##---------------------------------- # sub menu - If Go back mode is selected.-------------------------------------------------------      
##-------------------------------------------------------------------------------------------------------------------------------------                            
                        
                elif option_1 == "3":
                    play = False                  
# ---------------------------------- # Exit Sub menu-------------------------------------------------------------------------------------      
# ____________________________________MAIN MENU SELECTED : 2. SHOW HISTORY _________________________________________________________________               

        elif choice == "2":
            my_history.print_stats()
            
#____________________________________MAIN MENU SELECTED : 3. RULES _________________________________________________________________               
        elif choice == "3":
            display.game_rules()
#___________________________________MAIN MENU SELECTED : 4. RESTART _________________________________________________________________               

        elif choice == "4":
            pass
#____________________________________MAIN MENU SELECTED : 5. CHANGE NAME _________________________________________________________________               

        elif choice == "5":
            existing_name = input("Enter exisitng name: ")
            change_name = input("Enter the desired name: ")
            my_player.change_name(existing_name, change_name)
            my_history.stats_update_name_change(existing_name, change_name)      
        
#____________________________________MAIN MENU SELECTED : 6. QUIT _________________________________________________________________               
        elif choice == "6":
            my_player.save_players_list()
            my_history.save_players_dict()
            keep_running = False   
    
def sub_menu_1_execute(my_player):
    new_or_existing_player = True
    while new_or_existing_player:
        display.sub_menu_1()                                    # New or existing player ?
        option_2 = input("Enter your choice (1-2): ")
        
        if option_2 > "2" or option_2 < "1":
            print("Invalid input. Please enter a number (1-2).")                         
        elif option_2 == "1":
            player_1, x = new_player_menu_execute(my_player)
            new_or_existing_player = False
            return player_1, x 
        elif option_2 == "2": 
            old_name = input("Provide Player Name: ")                   #Exisiting player
            a = my_player.search_player(old_name)
            if a == "1":
                new_or_existing_player = True
            else:
                return a, 'Start'
        # elif option_2 == "3":
        #     new_or_existing_player = False
        #     return 'Go Back'
    
        
def new_player_menu_execute(my_player):           
    new_player = True
    while new_player:
        new_name = input("Enter name to create Player: ")                   #New Player
        a = my_player.create_player(new_name)
        if a == "1":
            new_player = True
        else:
            new_player = False
            return new_name, 'Start'
            

def hold_or_roll(my_dice, pig_game):
    roll = ''
    while roll != 'h':
        print("Enter 'Q/q' anytime to restart the game.")
        roll = input("Enter 'R/r' to roll dice & 'H/h' to hold.")
        value = pig_game.roll_or_hold(my_dice, roll)
        return value

def play_logic(pig_game, current_player, p1_instance, p2_instance):
    display.switch_display()                                
    pig_game.scoreboard(p1_instance, p2_instance)         
    
    current_player = pig_game.switch(
        current_player, p1_instance, p2_instance)
    
    pig_game.print_current_player(current_player)

if __name__ == "__main__":
    main()                   