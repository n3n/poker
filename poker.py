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
	pass

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
    elif fullhouse(ranks):
        return 6, kind(3, ranks)
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

def full_house(hand):
	pass
	
def kind(hand):
	pass
	
def twopair(hand):
	pass
	
print flush(['JC', 'TC', '9C', '8C', '7C'])
