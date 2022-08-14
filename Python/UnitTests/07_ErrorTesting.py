# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 14:58:14 2022

@author: Krystian
"""

"""
assertRaises(exception, callable, *args, **kwargs)
    testuje czy błąd zostanie wyrzucony. Test jest zdany, gdy oczekiwany błąd
    zostanie podniesiony, w przeciwnym razie test jest nie zdany
"""

import unittest


def div(a, b):
    return a / b


class RaiseTest(unittest.TestCase):
    
    def test_raise(self):
        self.assertRaises(ZeroDivisionError, div, 1, 0)
        
        
if __name__ == '__main__':
    unittest.main()
    
