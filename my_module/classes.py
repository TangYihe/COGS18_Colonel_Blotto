"""The Colonel Blotto class

Each instance records an arrangment and its total score 
when battling against our sample population.

Attributes
-------------
arrangement: array. The knight arrangement in castles
score: int. The total score battling against sample population.

Methods
-------------
__init__(): instance initialization

set_arr(), get_arr(), set_score(),get_score():
        getters and setters for instance attributes

battle(self, adversary): performing battle between the arrangement of 
current instance and an adversary.
    Parameters
    -----------
    self: current CB instance
    adversary: CB instance that we want to battle to
    
    Returns
    -----------
    list of size 2. First element represents how many points current 
    instance earns from this battle, second elements represents how
    many points adversary earns from this battle.
"""

class CBInstance():
    
    def __init__(self, arrangement):
        
        self.arrangement = arrangement
        self.score = 0 
        
    def set_arr(self, arrangement):
        
        self.arrangement = arrangement
        
    def get_arr(self):
        
        return self.arrangement
    
    def set_score(self, score):
        
        self.score = score
        
    def get_score(self):
        
        return self.score
    
    def battle(self, adversary):
        
        # To keep track of number of castles each wins
        self_win = 0
        adv_win = 0
        
        # Compare and record how many castle each arrangements wins
        for ind in range(len(self.arrangement)):
            
            if(self.arrangement[ind] > adversary.arrangement[ind]):
                self_win = self_win + 1
            elif(self.arrangement[ind] < adversary.arrangement[ind]):
                adv_win = adv_win + 1
        
        # Decides which wins the battle and assign points accordingly
        if(self_win > adv_win):
            return [1,0]
        elif(self_win == adv_win):
            return [0.5, 0.5]
        else:
            return [0,1]
