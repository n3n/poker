import unittest
import poker
 
class TestPoker(unittest.TestCase):
	'''Example unittest test methods for poker.'''
 
 	def poker(self):
		'''Test poker with [['JC', 'TC', '9C', '8C', '7C'],['JS', 'TS', '9S', '8S', '7S']]'''
		
		actual = poker.poker([['JC', 'TC', '9C', '8C', '7C'],['JS', 'TS', '9S', '8S', '7S']])
		expected = [['JC', 'TC', '9C', '8C', '7C'], ['JS', 'TS', '9S', '8S', '7S']]
		self.assertEqual(actual, expected)
		
	def straight_flush(self):
		'''Test straight flush with ['JC', 'TC', '9C', '8C', '7C']'''
		
		actual = poker.straight_flush(['JC', 'TC', '9C', '8C', '7C'])
		expected = True
		self.assertEqual(actual, expected)

	def straight(self):
		'''Test straight with ['5S', '5H', '5D', '5C', 'KS']'''
		
		actual = poker.straight(['5S', '5H', '5D', '5C', 'KS'])
		expected = False
		self.assertEqual(actual, expected)
		
	def flush(self):
		'''Test flush with ['5C', 'TC', '9C', '3C', '7C']'''
		
		actual = poker.flush(['5C', 'TC', '9C', '3C', '7C'])
		expected = True
		self.assertEqual(actual, expected)
		
	def full_house_F(self):
		'''Test full_house (False) with ['5C', 'TC', '9C', '3C', '7C']'''
		
		actual = poker.full_house(['5C', 'TC', '9C', '3C', '7C'])
		expected = False
		self.assertEqual(actual, expected)
	
	def full_house_T(self):
		'''Test full_house (True) with ['5C', '5S', '5H', '3C', '3H']'''
		
		actual = poker.full_house(['5C', '5S', '5H', '3C', '3H'])
		expected = True
		self.assertEqual(actual, expected)
		
	def kind(self):
		'''Test 3 of kind with ['4C', '4S', '4H', '3C', '7C']'''
		
		actual = poker.kind(['4C', '4S', '4H', '3C', '7C'])
		expected = True
		self.assertEqual(actual, expected)
		
	def two_pair(self):
		'''Test twopair with ['5C', 'AS', '2C', '3C', '5H']'''
		
		actual = poker.twopair(['5C', 'AS', '2C', '3C', '5H'])
		expected = True
		self.assertEqual(actual, expected)
	
if __name__ == '__main__':
	unittest.main(exit=False)
