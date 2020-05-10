# -*- coding: utf-8 -*-
"""
Created on Mon May  4 23:10:56 2020

@author: Gerard
"""

import unittest
from CA3 import Calculator


class CalculatorTest(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator()
        pass
    
    def test_add(self):
        calc = Calculator()
        a = [5]    
        b = [5]
        c= [-5]
        d = [-10]
        e = [10]

        self.assertEqual([10], list(calc.add(a,b)))
        self.assertEqual([0], list(calc.add(a,c)))
        self.assertEqual([-5], list(calc.add(a,d)))
        self.assertEqual([5], list(calc.add(c,e)))

    def test_subtract(self):
        calc = Calculator()
        a = [5]    
        b = [5]
        c= [-5]
        d = [-10]
        e = [10]
        f = [0]
        self.assertEqual([0], list(calc.subtract(a,b)))
        self.assertEqual([10], list(calc.subtract(a,c)))
        self.assertEqual([-15], list(calc.subtract(d,a)))
        self.assertEqual([5], list(calc.subtract(e,a)))
        self.assertEqual([5], list(calc.subtract(a,f)))

    def test_square(self):
        calc = Calculator()
        a = [0]    
        b = [5]
        c= [-5]
        d = [2,3]

        self.assertEqual([0], list(calc.square(a)))
        self.assertEqual([25], list(calc.square(b)))
        self.assertEqual([25], list(calc.square(c)))
        self.assertEqual([4,9], list(calc.square(d)))

    def test_cube(self):
        calc = Calculator()
        a = [0]    
        b = [5]
        c= [-5]
        d = [2,3]

        self.assertEqual([0], list(calc.cube(a)))
        self.assertEqual([125], list(calc.cube(b)))
        self.assertEqual([-125], list(calc.cube(c)))
        self.assertEqual([8,27], list(calc.cube(d)))

    def test_odd(self):
        calc = Calculator()
        a = [0,1,2,3,4,5,6]    
        self.assertEqual([1,3,5], list(calc.odd(a)))

    def test_even(self):
        calc = Calculator()
        a = [0,1,2,3,4,5,6]    
        self.assertEqual([0,2,4,6], list(calc.even(a)))

    # I didn't test for factorial of numbers less than 1 as the def is set up to calculate
    # on a range starting at 1. User entered numbers less than zero are forced to 
    # enter again
    def test_factorial(self):
        calc = Calculator()
        a = 1
        b = 2
        c = 3
        d = 4
        self.assertEqual(1, calc.factor(a))
        self.assertEqual(2, calc.factor(b))
        self.assertEqual(6, calc.factor(c))
        self.assertEqual(24, calc.factor(d))

    def test_squareRoot(self):
        calc = Calculator()
        self.assertEqual([1.0, 1.4142135623730951], list(calc.squareRoot(range(1,3))))

    # test for fibanacci numbers definition
    def test_fibonnaci(self):
        calc = Calculator()
        self.assertEqual([0, 1, 1, 2, 3], list(calc.fibonacci(4)))
        self.assertEqual([0, 1], list(calc.fibonacci(1)))
        self.assertEqual([0], list(calc.fibonacci(0)))

    # calculating the percentages by iterating values in one list over another
    def test_percent(self):
        calc = Calculator()
        a = [3, 1, 3]
        b = [5, 4, 10]
        c = [10]    
        d = [5]
        e= [-5]
        self.assertEqual([60, 25, 30], list(calc.percent(a,b)))
        self.assertEqual([50], list(calc.percent(d,c)))
        self.assertEqual([-50], list(calc.percent(e,c)))

       
    # test for max   
    def test_max(self):
        calc = Calculator()
        a = [1, 2, 3, 4]
        b = [-4, -3, -2, -1]
        c = [-4, -3, -2, 0]
        self.assertEqual(4, calc.max(a))
        self.assertEqual(-1, calc.max(b))
        self.assertEqual(0, calc.max(c))

# 
if __name__ == '__main__':
    unittest.main()    
