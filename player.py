class Player:
    
    def __init__(self, name):
        self.name = name 
        self.score = 0
        self.tempscore = 0
        self.wins = 0 
        self.loss = 0 
        self.count_of_games_played = 0  
              
    def score1(self, roll_dice_num):        
        if roll_dice_num == 1:  # When the player rolled 1
            self.tempscore = 0 
        elif roll_dice_num == 0:   # When the player selected to hold            
            self.score += self.tempscore
            self.tempscore = 0
        else:   # When the player rolled 2 to 6
            self.tempscore += roll_dice_num
            if self.tempscore + self.score >= 100:
                self.score += self.tempscore
    
    def won(self):
        self.wins += 1
        self.count_of_games_played += 1
    
    def lost(self):
        self.loss += 1
        self.count_of_games_played += 1   
  

              