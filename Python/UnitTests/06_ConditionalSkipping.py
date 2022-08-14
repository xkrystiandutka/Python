# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 14:52:15 2022

@author: Krystian
"""

"""
Opis metod:
    
    unittest.skip(reason)
        pomija oznaczony test
    
    unittest.skipIf(condition, reason)
        pomija oznaczony test jeżeli warunek jest prawdziwy
        
    unittest.skipUnless(condition, reason)
        pomija oznaczony test, chyba, że warunek jest prawdziwy
        
    unittest.expectedFailure()
        oznacza test jako oczekiwany błąd, jeżeli test będzie niepowodzeniem
        nie zostanie policzony jako błąd.
"""
import unittest


class SimpleTest(unittest.TestCase):
    
    x = 6
    y = 8
    
    @unittest.skip('Skip')
    def testAdd(self):
        score = self.x + self.y
        self.assertEqual(score, 6)
    
    @unittest.skipIf(x < y, 'Skip')
    def testSub(self):
        score = self.x - self.y
        self.assertEqual(score, 2)
    
    @unittest.skipUnless(y == 0, 'Skip')
    def testDiv(self):
        score = self.x / self.y
        self.assertEqual(score, 3.0)
        
    @unittest.expectedFailure
    def testMul(self):
        score = self.x * self.y
        self.assertEqual(score, 10)


if __name__ == '__main__':
    unittest.main()    
        