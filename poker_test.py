import unittest
import poker
 
class TestPoker(unittest.TestCase):
	'''Example unittest test methods for poker.'''
 
 	def test_poker(self):
		'''Test poker with [['JC', 'TC', '9C', '8C', '7C'],['JS', 'TS', '9S', '8S', '7S']]'''
		
		actual = poker.poker([['JC', 'TC', '9C', '8C', '7C'],['JS', 'TS', '9S', '8S', '7S']])
		expected = [['JC', 'TC', '9C', '8C', '7C'], ['JS', 'TS', '9S', '8S', '7S']]
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
		'''Test full_house (False) with ['5C', 'TC', '9C', '3C', '7C']'''
		
		actual = poker.full_house(['5C', 'TC', '9C', '3C', '7C'])
		expected = False
		self.assertEqual(actual, expected)
	
	def test_full_house_2(self):
		'''Test full_house (True) with ['5C', '5S', '5H', '3C', '3H']'''
		
		actual = poker.full_house(['5C', '5S', '5H', '3C', '3H'])
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
					
	def test_twopair(self):
		'''Test twopair with ['5C', 'AS', '2C', '3C', '5H']'''
		
		actual = poker.twopair(['5C', 'AS', '2C', '3C', '5H'])
		expected = True
		self.assertEqual(actual, expected)
	

if __name__ == '__main__':
	unittest.main(exit=False)
