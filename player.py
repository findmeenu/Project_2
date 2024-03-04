class Player:
    
    def __init__(self, name):
        self.name = name 
        self.number_recd_dice = 0
        self.total_score = 0
        self.wins = 0 
        self.loss = 0 
        self.count_of_games_played = 0        
    
    def update_score(self, roll_dice_num):    
        if roll_dice_num == 1: 
            self.totalscore = 0   
        else:
            self.totalscore += roll_dice_num
            
    def get_total_score(self):
        return self.__totalscore
    
    def won(self):
        self.wins += 1
        self.count_of_games_played += 1
    
    def lost(self):
        self.loss += 1
        self.count_of_games_played += 1   
        
    def get_wins(self):
        return self.wins
    
    def get_losses(self):
        return self.loss
              