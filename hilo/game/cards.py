class Cards:

    """
    The 'Cards' class will be the stack of cards in the deck. It will have
    all 52 cards from their respective suits. This inteded to be used by
    the 'Dealer' so that it has cards to choose from.

    Attributes:
            deck: A list of all 52 cards in a deck.
            last_card: remebers the last card used by the 'Dealer'.
    Methods:
            deck_build:
                    Builds the deck.
            shuffle: when a new card goes into last_card, the old card
                     will be put back in the deck. It is 'shuffled'
                     back into the deck.
    """
    def __init__(self):
        self.deck = dict()
        self.last_card = 0
        self.shuffledDeck = dict()

    def deck_build(self):
        tempDict = dict()
        cardNumber = 1
        suits = ["C","D","H","S"]
        for i in range(0,4):
            for l in range(1,14):
                card = suits[i] + str(l)
                tempDict[cardNumber] = card
                cardNumber += 1
        self.deck = tempDict

    def shuffle(self,choice):
        self.last_card = choice
        self.shuffledDeck = {key:val for key, val in self.deck.items()
        if key != self.last_card}
