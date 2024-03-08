
import random

class Game:
    
                 
    def roll_first(self, p1_name, p2_name):
        a = random.choice(['Heads', 'Tails'])
        if a == 'Heads':  
            return p1_name
        else:
            return p2_name
             
    # create two player objects & decides based on coin toss who will
    # roll the play first.
    def first_player(self, player_name, p1_instance, p2_instance):  # 
        if player_name == p2_instance.name:
            current_player = p2_instance
            # print("1")
        elif player_name == p1_instance.name:
            current_player = p1_instance
        print(f"\n{current_player.name} will play first.\n")   #print("2")
        return current_player       

        
    def scoreboard(self, p1_instance, p2_instance):
        print(f"{p1_instance.name} ----------------> {p1_instance.score}")
        print(f"{p2_instance.name} ----------------> {p2_instance.score}")
        print()
                
    def switch(self, current_player, p1_instance, p2_instance):
        if current_player == p1_instance:
            current_player = p2_instance
        else:
            current_player = p1_instance
        return current_player    

    def print_current_player(self, current_player_instance):
        print(f"{current_player_instance.name} turn now. Ready to Roll ! ")
        print("-" * 100)
        
    
    def roll_or_hold(self, my_dice, roll):
        if roll.lower() == 'r':
            value = my_dice.roll()
            return value
        elif roll.lower() == 'h':
            print("\n Another player turn.\n")
            return 0
        elif roll.lower() == 'q':
            print("Restarting the Game.")
            return 2000

