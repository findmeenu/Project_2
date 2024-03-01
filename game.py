# Game Rules 
# Who will roll first

# # check if the player exist 
# shuld handle player switch
import time
import os
import random

class Game:
    
    def __init__(self):
        
    def game_rules(self):    
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
        
    def roll_first (self, p1_name, p2_name):
         a= random.choice(['Heads', 'Tails'])
         if a == 'Heads':
             print("P1 will roll first" + p1_name)
         else:
             print("P1 will roll first" + p2_name)
             
    def start_game():
        