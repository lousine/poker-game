from poker_desk import Poker_Deck
import math

class Poker (object):
  """
    Combination are ranked as follows (from high to low):
  --- Royal (Royal is the highest possible hand. If more than one hand has Royal, the higher card wins (Five Aces beats five kings, which beat five queens, and so on).
Straight Flush)
  --- Straight Flush (A straight flush is the best natural hand. A straight flush is a straight (5 cards in order, such as 5-6-7-8-9) that are all of the same suit. As in a regular straight, you can have an ace either high (A-K-Q-J-T) or low (5-4-3-2-1). However, a straight may not 'wraparound'.)
  --- Four of a Kind (Four of a kind is simply four cards of the same rank. If there are two or more hands that qualify, the hand with the higher-rank four of a kind wins. If, in some bizarre game with many wild cards, there are two four of a kinds with the same rank, then the one with the high card outside the four of the kind wins.)
  --- Full House (A full house is a three of a kind and a pair, such as K-K-K-5-5. Ties are broken first by the three of a kind, then pair. So K-K-K-2-2 beats Q-Q-Q-A-A, which beats Q-Q-Q-J-J.)
  --- Flush (A flush is a hand where all of the cards are the same suit, such as J-8-5-3-2, all of spades.)
  --- Straight (A straight is 5 cards in order, such as 4-5-6-7-8. An ace may either be high (A-K-Q-J-T) or low (5-4-3-2-1). However, a straight may not 'wraparound'. (Such as Q-K-A-2-3, which is not a straight). When straights tie, the highest straight wins.)
  --- Three of a Kind (Three cards of any rank, matched with two cards that are not a pair (otherwise it would be a Full House . )
  --- Two Pair (This is two distinct pairs of card and a 5th card. The highest pair wins ties. If both hands have the same high pair, the second pair wins. If both hands have the same pairs, the high card wins.)
  --- Pair (One pair with three distinct cards. High card breaks ties.)
  --- High Card (This is any hand which doesn't qualify as any one of the above hands. If nobody has a pair or better, then the highest card wins. If multiple people tie for the highest card, they look at the second highest, then the third highest etc. High card is also used to break ties when the high hands both have the same type of hand (pair, flush, straight, etc).)
  """
  def __init__ (self, numPlayers):
      
    card_quant = 5

    self.players = []
    self.list_t=[]
    self.deck = Poker_Deck()
    self.deck.shuffle ()

    for i in range (numPlayers):
      player = []
      for j in range (card_quant):
        player.append (self.deck.deal())
      self.players.append (player)
  
  def play (self):
    for i in range (len (self.players) ):
      s_Player = sorted (self.players[i], reverse = True)
      player = ""
      for card in s_Player:
        player = player + str(card) + " "
      print ("Player " + str(i + 1) + " holds " + player)

  def amount(self,player):                         
    s_Player=sorted(player,reverse=True)
    c_sum=0
    ranks=[]
    for card in s_Player:
      ranks.append(card.rank)
    c_sum=ranks[0]*13**4+ranks[1]*13**3+ranks[2]*13**2+ranks[3]*13+ranks[4]
    return c_sum

  def High (self, player):                          
    s_Player=sorted(player,reverse=True)
    logic=True
    h=1
    tot_amount=h*13**5+self.amount(s_Player)
    sequence=[]                                       
    for card in s_Player:
      sequence.append(card.rank)
    print ("High Card")
    self.list_t.append(tot_amount)
    
  def One (self, player):                            
    s_Player=sorted(player,reverse=True)
    logic=True
    h=2
    tot_amount=h*13**5+self.amount(s_Player)
    sequence=[]                                       
    mycount=[]                                      
    for card in s_Player:
      sequence.append(card.rank)
    for each in sequence:
      count=sequence.count(each)
      mycount.append(count)
    if mycount.count(2)==2 and mycount.count(1)==3:  
      logic=True
      print ("One Pair")
      self.list_t.append(tot_amount)
      
    else:
      logic=False
      self.High(s_Player)

  def Two (self, player):                          
    s_Player=sorted(player,reverse=True)
    logic=True
    h=3
    tot_amount=h*13**5+self.amount(s_Player)
    rank1=s_Player[1].rank                        
    rank2=s_Player[3].rank
    sequence=[]
    for card in s_Player:
      sequence.append(card.rank)
    if sequence.count(rank1)==2 and sequence.count(rank2)==2:
      logic=True
      print ("Two Pair")
      self.list_t.append(tot_amount)
      
    else:
      logic=False
      self.One(s_Player)      

  def Three (self, player):
    s_Player=sorted(player,reverse=True)
    logic=True
    h=4
    tot_amount=h*13**5+self.amount(s_Player)
    Currank=s_Player[2].rank
    sequence=[]
    for card in s_Player:
      sequence.append(card.rank)
    if sequence.count(Currank)==3:
      logic=True
      print ("Three of a Kind")
      self.list_t.append(tot_amount)
      
    else:
      logic=False
      self.Two(s_Player) 

  def Straight (self, player):
    s_Player=sorted(player,reverse=True)
    logic=True
    h=5
    tot_amount=h*13**5+self.amount(s_Player)
    Currank=s_Player[0].rank                        
    for card in s_Player:
      if card.rank!=Currank:
        logic=False
        break
      else:
        Currank-=1
    if logic:
      print("Straight")
      self.list_t.append(tot_amount)
      
    else:
      self.Three(s_Player)      
      
  def Flush (self, player):                         
    s_Player=sorted(player,reverse=True)
    logic=True
    h=6
    tot_amount=h*13**5+self.amount(s_Player)
    Cursuit=s_Player[0].ctype
    for card in s_Player:
      if not(card.ctype==Cursuit):
        logic=False
        break
    if logic:
      print ("Flush")
      self.list_t.append(tot_amount)
      
    else:
      self.Straight(s_Player)   

  def Full (self, player):                     
    s_Player=sorted(player,reverse=True)
    logic=True
    h=7
    tot_amount=h*13**5+self.amount(s_Player)
    sequence=[]                                 
    for card in s_Player:
      sequence.append(card.rank)
    rank1=s_Player[0].rank                  
    rank2=s_Player[-1].rank
    num_rank1=sequence.count(rank1)
    num_rank2=sequence.count(rank2)
    if (num_rank1==2 and num_rank2==3)or (num_rank1==3 and num_rank2==2):
      logic=True
      print ("Full House")
      self.list_t.append(tot_amount)
      
    else:
      logic=False
      self.Flush(s_Player)

  def Four (self, player):                  
    s_Player=sorted(player,reverse=True)
    logic=True
    h=8
    Currank=s_Player[1].rank               
    count=0
    tot_amount=h*13**5+self.amount(s_Player)
    for card in s_Player:
      if card.rank==Currank:
        count+=1
    if not count<4:
      logic=True
      print("Four of a Kind")
      self.list_t.append(tot_amount)

    else:
      self.Full(s_Player)

  def StraightFlush (self, player):       
    s_Player=sorted(player,reverse=True)
    logic=True
    h=9
    Cursuit=s_Player[0].ctype
    Currank=s_Player[0].rank
    tot_amount=h*13**5+self.amount(s_Player)
    for card in s_Player:
      if card.ctype!=Cursuit or card.rank!=Currank:
        logic=False
        break
      else:
        Currank-=1
    if logic:
      print ("Straight Flush")
      self.list_t.append(tot_amount)
    else:
      self.Four(s_Player)
      
  def Royal (self, player):               
    s_Player=sorted(player,reverse=True)
    logic=True
    h=10
    Cursuit=s_Player[0].ctype
    Currank=14
    tot_amount=h*13**5+self.amount(s_Player)
    for card in s_Player:
      if card.ctype!=Cursuit or card.rank!=Currank:
        logic=False
        break
      else:
        Currank-=1
    if logic:
        print("Royal Flush")
        self.list_t.append(tot_amount)    
    else:
      self.StraightFlush(s_Player)
