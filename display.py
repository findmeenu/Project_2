import os
import time


def game_rules():    
        print("WELCOME ! \n")
        print("PIG : DICE GAME \n" )
        print("The Game Rules: \n") 
        print("Each turn, a player repeatedly rolls a dice until either a 1 is rolled or the player decides to \"hold\": \n") 
        print("-> If the player rolls a 1, they score nothing and it becomes the next player's turn.")
        print("-> If the player rolls any other number, it is added to their turn total and the player's turn continues.")
        print("-> If a player chooses to \"hold\", their turn total is added to their score, and it becomes the next player's turn. \n")
        print ("The first player to score 100 or more points wins.")
        time.sleep(1)
        os.system("cls")
        
def main_menu():
    print("\n-------Dice Game--------")            
    print("1. Play")
    print("2. Show History")
    print("3. Rules")
    print("4. Restart")    
    print("5. Change Name")
    print("6. Quit\n")      
    
def sub_menu_1():
    print("\n1. New Player")
    print("2. Existing Player\n")

def start_game():
        print("\nLet's begin Fun!")         
        
def switch_display():
    print("\nPLAYER SWITCHED. due to rolled 1")  
    print(f" Name  ----------------> Total Score")        