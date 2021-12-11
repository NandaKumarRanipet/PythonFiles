import unittest
from fibonacci import FibRecursion

class MyTest(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(FibRecursion(5),7)
    def test_fibonacci_1(self):
        self.assertEqual(FibRecursion(1),1)
    def test_fibonacci_1(self):
        self.assertEqual(FibRecursion("stringvalue"),1)
    
if __name__ == '__main__':
    unittest.main()
