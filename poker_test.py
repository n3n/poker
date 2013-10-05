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
		'''Test flush with ['8S', '6HC', '9C', '2D', '4H']'''
		
		actual = poker.flush(['8S', '6HC', '9C', '2D', '4H'])
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
		
	def test_kind(self):
		'''Test 3 of kind with ['4C', '4S', '4H', '3C', '7C']'''
		
		actual = poker.kind(['4C', '4S', '4H', '3C', '7C'])
		expected = True
		self.assertEqual(actual, expected)
		
	def test_twopair(self):
		'''Test twopair with ['5C', 'AS', '2C', '3C', '5H']'''
		
		actual = poker.twopair(['5C', 'AS', '2C', '3C', '5H'])
		expected = True
		self.assertEqual(actual, expected)
	

if __name__ == '__main__':
	unittest.main(exit=False)
