import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
  

  

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("This is not a palindrome"))

   

if __name__ == '__main__':
    unittest.main()