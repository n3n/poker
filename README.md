Poker Game Program
==================
This README file contains information about the poker game.

Game Mode
----------
 * SinglePlayer : You VS Bot game; shuffling five cards to each hand

General Rules
=============
A standard international 52-card pack is used, and in most forms of poker there are no jokers. 
The rank of the cards, from high to low, is A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2. In certain 
circumstances the ace can be used as a low card, below the 2.

There are four suits,(from high to low is S=spade,H=heart, D=diamond and C=club); normally no suit is higher than another, whenever a hand has the same hand ranking the suit is used to determine. 
All poker hands contain five cards, the highest hand wins. 

How the hands are ranked
------------------------
Hands are ranked as follows(from high to low):

* Royal Straight Flush
* Straight Flush
* Four of a kind
* Full House
* Flush
* Straight
* Three of a kind
* Two Pair
* One Pair
* High Card

**Note: When hands tie on the rank of a pair, three of a kind, etc, the cards outside break ties following the High Card rules.** 


Straight Flush
--------------
Five cards in sequence, all of the same suit. Two such hands are compared by their card that is ranked highest.Aces can be used as a low card, below the 2.

In the event of a tie: Highest rank at the top of the sequence wins.

Four of a kind
--------------
Four cards of the same rank, and one side card or 'kicker'.Quads with higher-ranking cards defeat lower-ranking ones.

In the event of a tie - Highest four of a kind wins.

Full House
----------
Three cards of the same rank, and two cards of a different matching rank.Between two full houses, the one with the higher-ranking three cards wins. 
If two hands have the same three cards, the hand with the higher pair wins.

Flush
-----
Five cards of the same suit, but not in sequence. Two flushes are compared as if they were high card hands; the highest-ranking card of each is compared to determine the winner. 

If both hands have the same highest card, then the second highest-ranking card is compared, and so on until a difference is found. If the two flushes contain the same five ranks of cards, when flushes ties, follow the rules for High Card.

Straight
--------
Five cards in sequence.

In the event of a tie - Highest ranking card at the top of the sequence wins.The ace may also be played as a low card (having a value of "1") 

Three of a kind
---------------
Three cards of the same rank and two unrelated side cards.

If two hands contain three of a kind of the same value, the kickers are compared to break the tie.

Two Pair
--------
2 pair of cards of a matching rank, another two cards of a different matching rank, and one side card.
To rank two hands both containing two pair, the higher-ranking pair of each is first compared, and the higher pair wins.

If both hands have the same top pair, then the second pair of each is compared. 

If both hands have the same two pairs, the kicker determines the winner.  

Pair
----
Two cards of a matching rank, and three unrelated side cards.
In the event of a tie - Highest pair wins. If hands have the same pair, the highest side card wins, and if necessary, the second-highest and third-highest side card can be used.


High Card
---------
Any hand that does not qualify under a category listed above.

In the event of a tie - Highest card wins, and if necessary up to fourth-highest and smallest card can be used to break the tie.

