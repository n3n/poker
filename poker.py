import os
import random

def poker(hands):
    """
   ([hand, hand, ...])-> hands
 
   Return the best hand from list of hands
   >>> sf = ['JC', 'TC', '9C', '8C', '7C']
   >>> fk = ['5S', '5H', '5D', '5C', 'KS']
   >>> sf2 = ['JS', 'TS', '9S', '8S', '7S']
   >>> poker([sf, sf2])
   [['JC', 'TC', '9C', '8C', '7C'], ['JS', 'TS', '9S', '8S', '7S']]
   >>> poker([sf, fk])
   [['JC', 'TC', '9C', '8C', '7C']]
   >>> fh = ['5S', '5H', '5D', '8C', '8S']
   >>> poker([fh, fk])
   [['5S', '5H', '5D', '5C', 'KS']]
   """
    return allmax(hands)
 
def gen_Card():
	"""
	generate 52 cards
	"""
	deck = []
	for rank in '23456789TJQKA':
		for suit in 'CDHS':
			deck.append(rank+suit)
	return deck

def allmax(hands):
    winhand = max(hands, key=hand_rank)
    maxval = hand_rank(winhand)
    return [hand for hand in hands if hand_rank(hand) == maxval]

def hand_rank(hand):
    """
   (hand)-> int
 
   Return the hand rank of a hand
   >>> sf = ['JC', 'TC', '9C', '8C', '7C']
   >>> hand_rank(sf)
   (8, 11)
   """
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    if ranks == [14,5,4,3,2]:
		ranks = [5,4,3,2,1]
       
    if straight_flush(hand):
        return 8, max(ranks)
    elif kind(4, ranks):
        return 7, kind(4, ranks)
    elif full_house(ranks):
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):
        return 5, ranks
    elif straight(hand):
        return 4, max(ranks)
    elif kind(3, ranks):
        return 3, kind(3, ranks)
    elif twopair(ranks):
        return 2, twopair(ranks)[0], twopair(ranks)[1], kind(1, ranks)
    elif kind(2, ranks):
        return 1, kind(2, ranks), ranks
    else:
        return 0, ranks
        
def royal_straight_flush(hand):
	
	return flush(hand)
	
def straight_flush(hand):
    """
   (hand)-> Bool
 
   Return True if hand is straight_flush,
   False otherwise
 
   >>> sf = ['JC', 'TC', '9C', '8C', '7C']
   >>> straight_flush(sf)
   True
   >>> fk = ['5S', '5H', '5D', '5C', 'KS']
   >>> straight_flush(fk)
   False
   """
    return straight(hand) and flush(hand)
 
def straight(hand):
    """
   (hand)-> Bool
 
   Return True if hand is straight,
   false otherwise
 
   >>> sf = ['JC', 'TC', '9C', '8C', '7C']
   >>> straight(sf)
   True
   >>> fk = ['5S', '5H', '5D', '5C', 'KS']
   >>> straight(fk)
   False
   """
 
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    if ranks == [14,5,4,3,2]:
		ranks = [5,4,3,2,1]
  
    return max(ranks)-min(ranks) == 4 and len(set(ranks)) == 5  
 
def flush(hand):
    """
   (hand)-> Bool
 
   Return True if hand is flush, False otherwise.
 
   >>> sf = ['JC', 'TC', '9C', '8C', '7C']
   >>> flush(sf)
   True
   >>> fk = ['5S', '5H', '5D', '5C', 'KS']
   >>> flush(fk)
   False
   """
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def full_house(ranks):
   """
   (ranks)-> Bool
 
   Return True if hand is fullhouse,
   false otherwise
 
   >>> sf_ranks = [11, 10, 9, 8, 7]
   >>> full_house(sf_ranks)
   False
   >>> fh_ranks = [5, 5, 5, 8, 8]
   >>> full_house(fh_ranks)
   True
   """
   return True if kind(3, ranks) and kind(2, ranks) else False
	
def kind(n, ranks):
    """
   (ranks)-> int
 
   Return rank if hand is n kind,
   false otherwise
 
   >>> sf_ranks = [11, 10, 9, 8, 7]
   >>> kind(4, sf_ranks)
   0
   >>> fk_ranks = [5, 5, 5, 5, 13]
   >>> kind(4, fk_ranks)
   5
   """
   
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return 0
	
def twopair(ranks):
    """
   (ranks)-> tuple
 
   Return tuple of highpair and lowpair if hand is twopair,
   false otherwise
 
   >>> sf_ranks = [11, 10, 9, 8, 7]
   >>> twopair(sf_ranks)
   ()
   >>> tp_ranks = [5, 5, 9, 8, 8]
   >>> twopair(tp_ranks)
   (8, 5)
   """
    ranks.sort(reverse=True)
    high_pair = kind(2, ranks)
    ranks.sort()
    low_pair = kind(2, ranks)
    ranks.sort(reverse=True)
    if high_pair != low_pair:
        return (high_pair, low_pair)
    return ()

def singleplayer():
	deck = gen_Card()
	os.system("clear")
	print '|=============================================================================|'
	print '|     _____                                                                   |'
	print '|    / ____|                                                                  |'
	print '|   | |                __      __      ____      ____      _______            |'
	print '|   | |               |  |    |  |    /    \    |    \    |   ____|           |'
	print '|    \ \\     ______   |   \  /   |   /  __  \   |  _  \   |  |____            | '
	print '|      \ \\  [______]  |    \/    |  |  |  |  |  | | \  |  |  ____ |           |'
	print '|       | |           |  |\  /|  |  |  |__|  |  | |_/  |  |   ____|           | '
	print '|   ____| |           |  | \/ |  |   \      /   |     /   |  |____            |'
	print '|  |_____/            |__|    |__|    \____/    |____/    |_______|           |'
	print '|                                                                             |'
	print '|=============================================================================|'
	
	name = raw_input("Enter name: ")
	
	gameplayer0, gameplayer1, gameplayer2, gameplayer3, i = [], [], [], [], 1
	for player in xrange(3):
		for card in xrange(5):
			card_num = random.randrange(0, 53-i)
			i += 1
			(eval('gameplayer%s' % str(player))).append(deck[card_num])
			deck.pop(card_num)
			random.shuffle(deck)		
	#print gameplayer0, gameplayer1, gameplayer2
	print poker([gameplayer0, gameplayer1, gameplayer2])
	
def multiplayer():
	pass
		
def game():
	"""
	game
	
	"""
	
	print "|------------------------------------------------------------|"
	print "|                         Poker Game                         |"
	print "|------------------------------------------------------------|"
	print "|          ____           _   __    ______    ______         |"
	print "|         |    |         | | / /   |  ____|  |      \        |"
	print "|         | [] |         | |/ /    | |____   |  [_]  |       |"
	print "|         |  __|   __    |   /     | ____ |  |    __/        |"
	print "|         | |     /  \   |   \     |  ____|  |  _ \          |"
	print "|         | |    | [] |  | |\ \    | |____   | | \_\         |"
	print "|         |_|     \__/   |_| \_\   |______|  |_|  \_\        |"
	print "|------------------------------------------------------------|"
	
	
	print "Select Mode: 1. SinglePlayer"
	print "             2. Multiplayer"
	mode = raw_input("Mode: ")
	if mode == '1':
		singleplayer()
	elif mode == '2':
		player = raw_input("enter player(2-4): ")
	else:
		os.system('clear')
		return "Exit"

#print twopair([11, 10, 9, 8, 7])
#print game()
#print poker([['JC', 'TC', '9C', '8C', '7C'],['5S', '5H', '5D', '5C', 'KS']])
#print poker([['9S', '8C', 'KC', '4S', 'TH'], ['8D', '4H', 'QS', '3C', 'JD']])
print singleplayer()
