import unittest
import poker
 
class TestPoker(unittest.TestCase):
	'''Example unittest test methods for poker.'''
 
 	def test_poker(self):
		'''Test poker with [['JC', 'TC', '9C', '8C', '7C'],['JS', 'TS', '9S', '8S', '7S']]'''
		
		actual = poker.poker([['JC', 'TC', '9C', '8C', '7C'],['JS', 'TS', '9S', '8S', '7S']])
		expected = [['JC', 'TC', '9C', '8C', '7C'], ['JS', 'TS', '9S', '8S', '7S']]
		self.assertEqual(actual, expected)
		
	def test_straight_flush(self):
		'''Test straight flush with ['JC', 'TC', '9C', '8C', '7C']'''
		
		actual = poker.straight_flush(['JC', 'TC', '9C', '8C', '7C'])
		expected = True
		self.assertEqual(actual, expected)

	def test_straight(self):
		'''Test straight flush with ['5S', '5H', '5D', '5C', 'KS']'''
		
		actual = poker.straight(['5S', '5H', '5D', '5C', 'KS'])
		expected = False
		self.assertEqual(actual, expected)
		
<<<<<<< HEAD
	def test_flush(self):
		'''Test straight flush with ['5C', 'TC', '9C', '3C', '7C']'''
		
		actual = poker.flush(['5C', 'TC', '9C', '3C', '7C'])
		expected = True
		self.assertEqual(actual, expected)
	
if __name__ == '__main__':
	unittest.main(exit=False)
=======

if __name__ == '__main__':
        unittest.main(exit=False)


>>>>>>> b7c1677ee0276ad330cea672d6994d6844210f5f
