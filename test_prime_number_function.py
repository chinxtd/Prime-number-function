import unittest
from prime_number_function import range_of_prime_number

class TestRangeOfPrimeNumber(unittest.TestCase):
    def test_range_of_prime_number_1(self):
        # Test case 1: Range from 1 to 10
        start_num = 1
        end_num = 10
        expected_result = [2, 3, 5, 7]
        result = range_of_prime_number(start_num, end_num)
        self.assertEqual(result, expected_result)

    def test_range_of_prime_number_2(self):
        # Test case 2: Range from 10 to 20
        start_num = 10
        end_num = 20
        expected_result = [11, 13, 17, 19]
        result = range_of_prime_number(start_num, end_num)
        self.assertEqual(result, expected_result)

    def test_range_of_prime_number_3(self):
        # Test case 3: Range from 20 to 30
        start_num = 20
        end_num = 30
        expected_result = [23, 29]
        result = range_of_prime_number(start_num, end_num)
        self.assertEqual(result, expected_result)

    def test_range_of_prime_number_4(self):
        # Test case 4: Range from 30 to 40
        start_num = 30
        end_num = 40
        expected_result = [31, 37]
        result = range_of_prime_number(start_num, end_num)
        self.assertEqual(result, expected_result)

    def test_range_of_prime_number_5(self):
        # Test case 5: Range from 1 to 250
        start_num = 1
        end_num = 250
        expected_result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241]
        result = range_of_prime_number(start_num, end_num)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()