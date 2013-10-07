import unittest
import poker
 
class TestPoker(unittest.TestCase):
	'''Example unittest test methods for poker.'''
 
 	def test_poker_1(self):
		'''Test poker ('straight flush') with [['JC', 'TC', '9C', '8C', '7C'],['JS', 'TS', '9S', '8S', '7S']]'''
		
		actual = poker.poker([['JC', 'TC', '9C', '8C', '7C'],['JS', 'TS', '9S', '8S', '7S']])
		expected = ([['JC', 'TC', '9C', '8C', '7C'], ['JS', 'TS', '9S', '8S', '7S']], 'straight flush')
		self.assertEqual(actual, expected)

 	def test_poker_2(self):
		'''Test poker ('onepair') with [['9S', '8C', 'KC', '4S', '9H'], ['8D', '3H', 'QS', '3C', 'JD']]'''
		
		actual = poker.poker([['9S', '8C', 'KC', '4S', '9H'], ['8D', '3H', 'QS', '3C', 'JD']])
		expected = ([['9S', '8C', 'KC', '4S', '9H']], 'onepair')
		self.assertEqual(actual, expected)

	def test_poker_3(self):
		'''Test poker ('straight flush') with [['AC', 'KC', 'QC', 'JC', 'TC'], ['AS', 'KS', 'QS', 'JS', 'TS']]'''
		
		actual = poker.poker([['AC', 'KC', 'QC', 'JC', 'TC'], ['AS', 'KS', 'QS', 'JS', 'TS']])
		expected = ([['AC', 'KC', 'QC', 'JC', 'TC'], ['AS', 'KS', 'QS', 'JS', 'TS']], 'straight flush')
		self.assertEqual(actual, expected)
		
	def test_poker_4(self):
		'''Test poker ('full house') with [['TS', 'KC', 'KS', 'KH', 'TC'], ['AC', '6S', '4D', '8H', 'TC']]'''
		
		actual = poker.poker([['TS', 'KC', 'KS', 'KH', 'TC'], ['AC', '6S', '4D', '8H', 'TC']])
		expected = ([['TS', 'KC', 'KS', 'KH', 'TC']], 'full house')
		self.assertEqual(actual, expected)

	def test_poker_5(self):
		'''Test poker ('flush') with [['TS', 'KS', '6S', '7S', 'QS'], ['AC', '2S', '4D', '8H', 'TC']]'''
		
		actual = poker.poker([['TS', 'KS', '6S', '7S', 'QS'], ['AC', '2S', '4D', '8H', 'TC']])
		expected = ([['TS', 'KS', '6S', '7S', 'QS']], 'flush')
		self.assertEqual(actual, expected)
		
	def test_royal_straight_flush(self):
		'''Test royal straight flush with ['AC', 'KC', 'QC', 'JC', 'TC']'''
		
		actual = poker.straight_flush(['AC', 'KC', 'QC', 'JC', 'TC'])
		expected = True
		self.assertEqual(actual, expected)	
		
	def test_straight_flush_1(self):
		'''Test straight flush with ['JC', 'TC', '9C', '8C', '7C']'''
		
		actual = poker.straight_flush(['JC', 'TC', '9C', '8C', '7C'])
		expected = True
		self.assertEqual(actual, expected)
		
	def test_straight_flush_2(self):
		'''Test straight flush with ['AH', '5H', '4H', '3H', '2H']'''
		
		actual = poker.straight_flush(['AH', '5H', '4H', '3H', '2H'])
		expected = True
		self.assertEqual(actual, expected)

	def test_straight_1(self):
		'''Test straight with ['5S', '2H', '3D', '4C', '6S']'''
		
		actual = poker.straight(['5S', '2H', '3D', '4C', '6S'])
		expected = True
		self.assertEqual(actual, expected)

	def test_straight_2(self):
		'''Test straight with ['AS', '8C', '2S', '4H', '8D']'''
		
		actual = poker.straight(['AS', '8C', '2S', '4H', '8D'])
		expected = False
		self.assertEqual(actual, expected)
		
	def test_flush_1(self):
		'''Test flush with ['5C', 'TC', '9C', '3C', '7C']'''
		
		actual = poker.flush(['5C', 'TC', '9C', '3C', '7C'])
		expected = True
		self.assertEqual(actual, expected)
		
	def test_flush_2(self):
		'''Test flush with ['8S', '6H', '9C', '2D', '4H']'''
		
		actual = poker.flush(['8S', '6H', '9C', '2D', '4H'])
		expected = False
		self.assertEqual(actual, expected)
		
	def test_full_house_1(self):
		'''Test full_house (False) with [11, 10, 9, 8, 7]'''
		
		actual = poker.full_house([11, 10, 9, 8, 7])
		expected = False
		self.assertEqual(actual, expected)
	
	def test_full_house_2(self):
		'''Test full_house (True) with [5, 5, 5, 8, 8]'''
		
		actual = poker.full_house([5, 5, 5, 8, 8])
		expected = True
		self.assertEqual(actual, expected)
		
	def test_three_of_kind_1(self):
		'''Test three of kind with [4, 4, 4, 3, 7]'''
		
		actual = poker.kind(3, [4, 4, 4, 3, 7])
		expected = 4
		self.assertEqual(actual, expected)
		
	def test_three_of_kind_2(self):
		'''Test three of kind with [4, 4, 7, 3, 2]'''
		
		actual = poker.kind(3, [4, 4, 7, 3, 2])
		expected = 0
		self.assertEqual(actual, expected)
	
	def test_four_of_kind_1(self):
		'''Test four of kind with [11, 10, 9, 8, 7]'''
		
		actual = poker.kind(4, [11, 10, 9, 8, 7])
		expected = 0
		self.assertEqual(actual, expected)

	def test_four_of_kind_2(self):
		'''Test four of kind with [9, 4, 9, 9, 9]'''
		
		actual = poker.kind(4, [9, 4, 9, 9, 9])
		expected = 9
		self.assertEqual(actual, expected)
	
	def test_one_pair_1(self):
		'''Test four of kind with [9, 4, 9, 8, 6]'''
		
		actual = poker.kind(2, [9, 4, 9, 8, 6])
		expected = 9
		self.assertEqual(actual, expected)

	def test_one_pair_2(self):
		'''Test four of kind with [11, 4, 2, 2, 9]'''
		
		actual = poker.kind(2, [11, 4, 2, 2, 9])
		expected = 2
		self.assertEqual(actual, expected)			
			
	def test_twopair_1(self):
		'''Test twopair with [11, 10, 9, 8, 7]'''
		
		actual = poker.twopair([11, 10, 9, 8, 7])
		expected = ()
		self.assertEqual(actual, expected)

	def test_twopair_2(self):
		'''Test twopair with [5, 5, 9, 8, 8]'''
		
		actual = poker.twopair([5, 5, 9, 8, 8])
		expected = (8, 5)
		self.assertEqual(actual, expected)


if __name__ == '__main__':
	unittest.main(exit=False)
