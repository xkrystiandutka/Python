# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 14:17:29 2022

@author: Krystian
"""

import unittest

def add(x, y):
    return x + y
    
class SimpleTest(unittest.TestCase):
    
    def testAdd(self):
        self.assertEqual(add(3,10), 8, msg='should be  13')
        

if __name__ == '__main__':
    unittest.main()