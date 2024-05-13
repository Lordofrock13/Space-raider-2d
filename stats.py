class Stats():
    def __init__(self):
    #Initialization of statistic
        self.reset_stats()
        self.run_game = True
    
    def reset_stats(self):
        #Changeable  ingame statistic 
        self.ship_left = 3
        self.score = 0