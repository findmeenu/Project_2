import random


class Dice:
    
    def __init__(self): 
        
        self.__sides = 6
        self.computer_easy_mode_option = [1, 1, 1, 1, 2, 3, 4, 5, 6]
    # ● ┌ ─ ┐ │ └ ┘
        self.__dice_art = {
                            1: ("┌─────────┐",
                                "│         │",
                                "│    ●    │",
                                "│         │",
                                "└─────────┘"),
                            2: ("┌─────────┐",
                                "│  ●      │",
                                "│         │",
                                "│      ●  │",
                                "└─────────┘"),
                            3: ("┌─────────┐",
                                "│  ●      │",
                                "│    ●    │",
                                "│      ●  │",
                                "└─────────┘"),
                            4: ("┌─────────┐",
                                "│  ●   ●  │",
                                "│         │",
                                "│  ●   ●  │",
                                "└─────────┘"),
                            5: ("┌─────────┐",
                                "│  ●   ●  │",
                                "│    ●    │",
                                "│  ●   ●  │",
                                "└─────────┘"),
                            6: ("┌─────────┐",
                                "│  ●   ●  │",
                                "│  ●   ●  │",
                                "│  ●   ●  │",
                                "└─────────┘")}   
         
    def roll(self): 
        rolled = random.randint(1, self.__sides)
        for line in self.__dice_art[rolled]:
            print(line)
        return rolled

    def roll_computer_easyMode(self):
        rolled = random.choice(self.computer_easy_mode_option)
        return rolled
    
    