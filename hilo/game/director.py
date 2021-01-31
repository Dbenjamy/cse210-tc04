from game.logic import Logic

print("made it this far")

class Director:
    """
    Controls the flow and execution of the game. Handles most endgame scenarios.
    Tracks and displays the points, gets most input from the user.

    NOTE FOR ME: "##" At the beginning and end of comment means replace with
                proper code. It is referencing a different class.

    Atrributes:
        keep_playing (boolean): does the player want to keep playing?
        points (int): Stores the number of points the player has.
            Player begins with 300 ponts.

    Methods:
        Constructor:
            defines primary and secondary attributes for method execution
        startGame:
            manages the beginning and ending of the game
        runGame:
            Controls the flow of the game
        endGame:
            Checks for and handles endgame scenarios
        computePoints:
            Tracks the number of points
    """
    def __init__(self):
        """The class constructor. Origin of the primary attributes

        Args:
            Self: an instance of director
        """

        #Used to recieve high or low result from logic()
        self.result = Logic()

        #Used to control the beginning and end of game
        self.keep_playing = True

        #Used to store the cards 
        self.card1 = 1  ## .dealer.getCard()##
        self.card2 = 2  ## .dealer.getCard()##

        #tracks the points
        self.points = 300


    def startGame(self):
        """Controls the flow of the game.

        Args:
            Self: an instance of Director
        """
        #Loop will run the game
        while self.keep_playing == True:
            self.runGame()
            self.endGame() #checks for end game scenarios before continuing

    def runGame(self):
        """Excutes the game. Calls necessary methods and prompts user for input.

        Args:
            Self: an instance of Director
        """

        # first round of the game
        # this block of code should only be executed once
        round = 0
        if round == 0:
            self.card1 ## .dealer.getCard()##
            round += 1
        else:
            pass

        
        self.card2 ## .dealer.getCard()##

        #display card1
        print("The card is: ", self.card1)

        #computePoints will ask Logic() to get h or l from user
        self.computePoints()

        #display card2
        print("Next card was: ", self.card2)

        #display points
        print("Your score is: ", self.points)

        #card2 becomes card1 for the next round
        ## Do we need this line here? Or is this taken care of elsewhere? ##
        self.card1 = self.card2

    def endGame(self):
        """Contains logic for end of game scenarios.
        Checks that the total number of points is greater than 0 before
        prompting for the users decision.

        Args:
            Self: An instance of Director
        """
        # Does the player have enough points?
        if self.points == 0:
            self.points = 0 #sets the points to 0
            print("You ran out of points. Better luck next time!")
            self.keep_playing = False

        #Does the user wish to continue playing?
        elif self.points > 0:
            again = input("Keep playing? [y/n] ")
            if (again == "n"):
                self.keep_playing = False
            else:
                pass
        #Enough points and user continues
        else:
            self.keep_playing = True

    def computePoints(self):
        """Computes the new point total using the input from Logic().
        Should only be reference once per run.

        Args:
            Self: An instance of Director
        """
        #ask logic for guess result
        guess = self.result.high_low(self.card1, self.card2)

        # check the boolean from Logic() and calculate points
        if guess == True:
            self.points += 100
        elif guess == False:
            self.points -= 75

