import unittest

class TestResult(unittest.TestCase):
    def test_result_prime_1_250(self):
        # get time prime number from the result.txt file
        with open("result.txt", "r") as file:
            result_prime_number = [int(line.strip()) for line in file]
        
        # expected prime number from 1 to 250
        expected_result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241]

        # check if it's true
        self.assertEqual(result_prime_number, expected_result)

if __name__ == "__main__":
    unittest.main()