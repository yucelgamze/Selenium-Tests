import unittest
from mathematics import Mathematics

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.math = Mathematics()

    def test_add(self):
        result = self.math.sumTwoNumbers(10,5) # matematik objesi oluşturulmalı test etmek için
        self.assertEqual(15, result)  # add assertion here

    def test_multiply(self):
        result = self.math.multiplyTwoNumbers(10,10)
        self.assertEqual(100, result)

    def tearDown(self) -> None:
        pass
if __name__ == '__main__':
    unittest.main()
