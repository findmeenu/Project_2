class Player:
    
    def __init__(self, name):
        self.name = name 
        self.score = 0
        self.target = 100
        self.filename = 'players.txt'
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
            
          
    
    def won(self):
        self.wins += 1
        self.count_of_games_played += 1
    
    def lost(self):
        self.loss += 1
        self.count_of_games_played += 1   
  

              