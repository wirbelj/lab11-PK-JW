# https://github.com/wirbelj/lab11-PK-JW.git
# Partner 1: Payton Keller
# Partner 2: Josalyn Wirbel
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code
    def test_add(self):
        from calculator import add
        assert(add(1,2) == 3)

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
    def test_subtract(self):
        from calculator import *
        assert(sub(3,2) == 1)


    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    def test_multiply(self):
        from calculator import *
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 5), -5)
        self.assertEqual(mul(0, 100), 0)

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################
    def test_divide(self):
        from calculator import *
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-6, 3), -2)
        self.assertEqual(div(5, 2), 2.5)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_divide_by_zero(self):
        from calculator import *
        with self.assertRaises(ZeroDivisionError):
            assert div(0,5)


    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    def test_logarithm(self):
        from calculator import *
        assert log(2,1)

    def test_log_invalid_base(self):
        from calculator import *
        with self.assertRaises(ValueError):
            assert log(1,0)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_log_invalid_argument(self):
        from calculator import *
        with self.assertRaises(ValueError):
            log(1, 10)
        with self.assertRaises(ValueError):
            log(-2, 8)
        with self.assertRaises(ValueError):
            log(2, -8)

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    def test_hypotenuse(self):
        from calculator import *
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

    def test_sqrt(self):
        from calculator import *
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(16), 4.0)
        with self.assertRaises(ValueError):
            square_root(-4)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
