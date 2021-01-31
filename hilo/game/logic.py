from game.director import Director

class Logic():
    """ 
    The key responsibility of the class is to prompt the user to choose
    if they would like to make their guess as either High or Low (H or L).
    This file will also talk to the Dealer class to tell it if the card
    was the same as the last card picked (in which it will end the game),
    or if the card is different, it will give the Dealer a boolean variable.
    
    Attributes: self.director
                self.choice
    Methods: high_low
    
    """

    def __init__(self):
        #passing in result of last card from Director
        self.director = Director()
        self.choice = False


    def high_low(self):
        # assuming that I am calling from a file named director
        # and that their Method is called current_card
        while self.director.result == True:
            decision = input('Higher or lower? [h/l]: ').lower()
            if decision == 'h':
                self.choice = True
                return self.choice

            elif decision == 'l':
                self.choice = False
                return self.choice
  
            else: 
            # if input is invalid
                print('Please try again and provide a correct value [h/l]')
