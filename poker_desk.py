import random
from card import Card

class Poker_Deck (object):
  """
  Poker is played from a standard pack of 52 cards.
  """
  def __init__ (self):
    self.deck = []
    for ctype in Card.poker_suits:
      for rank in Card.poker_ranks:
        card = Card (rank, ctype)
        self.deck.append(card)
        
  def deal (self): #Takes the last card in cards
    if len(self) == 0:
      return None
    else:
      return self.deck.pop(0)
  
  def __len__ (self):
    return len (self.deck)

  def shuffle (self):
    random.shuffle (self.deck)