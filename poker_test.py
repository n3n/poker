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
		
	def full_house(self):
		'''Test full_house with ['5C', 'TC', '9C', '3C', '7C']'''
		
		actual = poker.full_house(['5C', 'TC', '9C', '3C', '7C'])
		expected = True
		self.assertEqual(actual, expected)
		
	def kind(self):
		'''Test 3 of kind with ['5C', 'TC', '9C', '3C', '7C']'''
		
		actual = poker.kind(['5C', 'TC', '9C', '3C', '7C'])
		expected = True
		self.assertEqual(actual, expected)
		
	def two_pair(self):
		'''Test twopair with ['5C', 'TC', '9C', '3C', '7C']'''
		
		actual = poker.twopair(['5C', 'TC', '9C', '3C', '7C'])
		expected = True
		self.assertEqual(actual, expected)
	
if __name__ == '__main__':
	unittest.main(exit=False)
