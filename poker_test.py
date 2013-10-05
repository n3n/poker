import unittest
import poker
 
class TestPoker(unittest.TestCase):
	'''Example unittest test methods for poker.'''
 
	def test_poker_straight_flush(self):
		'''Test straight flush with ['JC', 'TC', '9C', '8C', '7C']'''
		
		actual = poker.straight_flush(['JC', 'TC', '9C', '8C', '7C'])
		expected = True
		self.assertEqual(actual, expected)
		
if __name__ == '__main__':
	unittest.main(exit=False)


