from random import randint
class Die :
    def __init__(self,num_dice =6) -> None:
        self.num_dice = num_dice
    def roll(self):

        return randint(1,self.num_dice)
     
    