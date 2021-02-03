class Cards:

    """
    The 'Cards' class will be the stack of cards in the deck. It will have
    all 52 cards from their respective suits. This inteded to be used by
    the 'Dealer' so that it has cards to choose from.

    Attributes:
            deck: A list of all 52 cards in a deck.
            last_card: remebers the last card used by the 'Dealer'.
    Methods:
            _deck_build:
                    Builds the deck.
            shuffle: when a new card goes into last_card, the old card
                     will be put back in the deck. It is 'shuffled'
                     back into the deck.
    """
    def __init__(self):
        self.keys = []
        self.deck = self._deck_build()
        self.last_card = 0
        self.shuffledDeck = {}
        self.shuffle(self)



    def _deck_build(self):
        tempDict = dict()
        self.keys = []
        cardNumber = 1
        suits = ["C","D","H","S"]
        for i in range(0,4):
            for l in range(1,14):
                card = suits[i] + str(l)
                tempDict[cardNumber] = card
                self.keys.append(cardNumber)
                cardNumber += 1
        return  tempDict

    def shuffle(self,choice=0):
        self.shuffledDeck = {key:val for key, val in self.deck.items()
        if key != self.last_card}
        self.last_card = choice
