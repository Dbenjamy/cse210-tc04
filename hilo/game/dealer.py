from hilo.game.cards import Cards
from hilo.game.director import Director
import random

class Dealer:
    def __init__(self):
        self.cards = Cards()
        
    def dealCards(self):
        randCard = random.randint(0, 52)
        return cards[randCard]