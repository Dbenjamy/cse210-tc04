from game.cards import Cards
import random

class Dealer:
    def __init__(self):
        self.cards = Cards()
        self.lastChoice = 0
        
    def dealCards(self):
        self.cards.shuffle(self.lastChoice)
        self.lastChoice = random.randint(1,52)
        try:
            return self.cards.shuffledDeck[self.lastChoice]
        except KeyError:
            return self.dealCards()
