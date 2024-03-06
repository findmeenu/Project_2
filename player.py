class Player:
    
    def __init__(self, name):
        self.name = name 
        self.score = 0
        self.target = 100
        self.filename = 'players.txt'
        
        
        #self.__total_score = 0
        self.wins = 0 
        self.loss = 0 
        self.count_of_games_played = 0  
              
    def score1(self, roll_dice_num):
                
        if roll_dice_num == 1:
            self.score += 0
            
            print(f"Check player method {self.score}")    
        else:
            print('FULL')
            print(self.score)
            print(roll_dice_num)
            self.score += roll_dice_num
            
            print(f"2..............Check player method {self.score}")
            
          
    
    # def update_score(self, roll_dice_num):    
    #     if roll_dice_num == 1: 
    #         self.totalscore = 0   
    #     else:
    #         self.totalscore += roll_dice_num
            
            
            
    def won(self):
        self.wins += 1
        self.count_of_games_played += 1
    
    def lost(self):
        self.loss += 1
        self.count_of_games_played += 1   
  #Getters-------------------------------------      
    def get_wins(self):
        return self.wins
    
    def get_losses(self):
        return self.loss
    
    def get_score(self):
        return self.score
    
    def get_total_score(self):
        return self.total_score
    
    def get_count_of_games_played(self):
        return self.count_of_games_played
    
    def get_name(self):
        return self.name
              
              
              

              