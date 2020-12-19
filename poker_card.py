class Card:
  """
  Poker is played from a standard pack of 52 cards. 
  (Some variant games use multiple packs or add a few cards called jokers.) 
  The cards are ranked (from high to low) Ace, King, Queen, Jack, 10, 9, 8, 7, 6, 5, 4, 3, 2, Ace. 
  (Ace can be high or low, but is usually high). 
  There are four suits (spades, hearts, diamonds and clubs); however, no suit is higher than another. 
  All poker hands contain five cards, the highest hand wins.
  """
  poker_ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  poker_suits = ("♠", "♢", "♡", "♣")

  def __init__ (self, rank, ctype):
    self.rank = rank
    self.ctype = ctype

  def __str__ (self):
    if self.rank == 11:
      rank = "Jack "
    elif self.rank == 12:
      rank = "Queen "
    elif self.rank == 13:
      rank = "King "
    elif self.rank == 14:
      rank = "Ace "
    else:
      rank = self.rank
    return str(rank) + self.ctype

  def __eq__ (self, o):
    return (self.rank == o.rank)

  def __ne__ (self, o):
    return (self.rank != o.rank)

  def __lt__ (self, o):
    return (self.rank < o.rank)

  def __le__ (self, o):
    return (self.rank <= o.rank)

  def __gt__ (self, o):
    return (self.rank > o.rank)

  def __ge__ (self, o):
    return (self.rank >= o.rank)