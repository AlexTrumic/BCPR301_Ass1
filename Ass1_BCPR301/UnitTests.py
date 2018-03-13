import unittest
import Cleaner
import Reader

class MainTests(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        self.x = 5

    def tearDown(self):
        # be executed after each test case
        pass #print('down')

    def test_03(self):
        print(3)
        self.assertTrue(self.x == 5, "the value of x should be 5!")

    def test_02(self):
        print(2)
        self.x = 6
        self.assertEqual(6, 3 * 2)

    def test_01(self):
        print(1)
        self.x = 6
        self.assertEqual(6, 6)

if __name__ == '__main__':
    unittest.main()