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

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

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

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
