from game import Cards
from hilo.game.director import Director
import random

class Dealer:
    def __init__(self):
        self.cards = Cards()
        lastChoice = 0
        
    def dealCards(self):
        lastChoice = random.randint(1,52)
        cards.shuffle(lastChoice)
        return cards.shuffledDeck[lastChoice]
        
