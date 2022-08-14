# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 14:38:12 2022

@author: Krystian
"""

"""
assertEqual - sprawdza czy dwa elementy są równe
assertNotEqual - sprawdza czy dwa elementy nie są równe
assertTrue - sprawdza czy wyrażenie/element jest prawdą
assertFalse - sprawdza czy wyrażenie/element jest fałszem
assertIn - sprawdza przynależnosc (czy należy)
assertNotIn - sprawdza przynależnosć (czy nie należy)
"""

import unittest


class SimpleTest(unittest.TestCase):
    
    def testAdd(self):
        self.assertEqual(3 + 7, 10)
    
    def testSub(self):
        self.assertNotEqual(8 - 3, 6)
        
    def testTrue(self):
        self.assertTrue(3 + 7 == 10)
        
    def testFalse(self):
        self.assertFalse(3 + 7 == 11)
        
    def testIn(self):
        self.assertIn(3, [1, 2, 3, 4])
        
    def testNotIn(self):
        self.assertNotIn(20, range(15))
        
        
if __name__ == '__main__':
    unittest.main()