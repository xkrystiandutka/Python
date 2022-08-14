# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 14:47:28 2022

@author: Krystian
"""

import unittest

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

class SimpleTest(unittest.TestCase):
    
    def testAdd(self):
        self.skipTest('Skip')
        self.assertEqual(add(4,5), 9)
        
    @unittest.skip('Skip')    
    def testSub(self):
        self.assertEqual(sub(10,8), 2)
        
if __name__ == '__main__':
    unittest.main()