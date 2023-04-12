import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_add(self):
        self.assertEqual(fizzbuzz.main(), [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'])

if __name__ == '__main__':
    unittest.main()