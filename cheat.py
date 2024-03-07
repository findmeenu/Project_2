import random


class Cheat:
    
    def __init__(self): 
        
        self.__sides = [1, 20, 30, 40, 50, 60]
        self.computer_easy_mode_option = [1, 1, 1, 1, 20, 30, 40, 50, 60]
    # ● ┌ ─ ┐ │ └ ┘
        self.__dice_art = {
                            1: ("┌─────────┐",
                                "│         │",
                                "│    ●    │",
                                "│         │",
                                "└─────────┘"),
                           20: ("┌─────────┐",
                                "│  ●      │",
                                "│         │",
                                "│      ●  │",
                                "└─────────┘"),
                           30: ("┌─────────┐",
                                "│  ●      │",
                                "│    ●    │",
                                "│      ●  │",
                                "└─────────┘"),
                           40: ("┌─────────┐",
                                "│  ●   ●  │",
                                "│         │",
                                "│  ●   ●  │",
                                "└─────────┘"),
                           50: ("┌─────────┐",
                                "│  ●   ●  │",
                                "│    ●    │",
                                "│  ●   ●  │",
                                "└─────────┘"),
                           60: ("┌─────────┐",
                                "│  ●   ●  │",
                                "│  ●   ●  │",
                                "│  ●   ●  │",
                                "└─────────┘")}   
         
    def roll(self): 
        rolled = random.choice(self.__sides)
        for line in self.__dice_art[rolled]:
            print(line)
        return rolled

    def roll_computer_easyMode(self):
        rolled = random.choice(self.computer_easy_mode_option)
        return rolled
    
   
   
       