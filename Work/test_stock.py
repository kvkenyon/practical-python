# test_stock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('AMZN', 100, 3400.0)
        self.assertEqual(s.name, 'AMZN')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 3400.0)
    
    def test_cost(self):
        s = stock.Stock('AMZN', 100, 3400.0)
        self.assertEqual(s.cost, 3400.0 * 100)

    def test_sell(self):
        s = stock.Stock('AMZN', 100, 3400.0)
        s.sell(25)
        self.assertEqual(s.shares, 75)
        self.assertEqual(s.cost, 3400.0 * 75)
    
    def test_bad_shares(self):
        s = stock.Stock('AMZN', 100, 3400.0)
        with self.assertRaises(TypeError):
            s.shares = 100.0

if __name__ == '__main__':
    unittest.main()