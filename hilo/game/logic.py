

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
        self.choice = False


    def high_low(self, card1, card2):
        # assuming that I am calling from a file named director
        # and that their Method is called current_card
        #while self.director.result == True:
        larger = "h"
        valid_input = False

        while valid_input == False:
            decision = input('Higher or lower? [h/l]: ')
            if decision == "h" or decision == "l":
                valid_input = True
                print("good input")
            else: 
                print('Please try again and provide a correct value [h/l]')

        if card1 > card2:
            larger = "h"
        elif card1 < card2:
            larger = "l"
        else:
            larger = "s"

            if (decision == 'h') and (larger == "h")  or (decision == "l") and (larger == "l"):
                self.choice = True
                return self.choice

            elif larger == "s":
                self.choice = False
                print("Cards match")
                return self.choice
            else:
                self.choice = False
                return self.choice

                