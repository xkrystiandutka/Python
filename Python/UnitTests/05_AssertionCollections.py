# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 14:42:47 2022

@author: Krystian
"""


"""
assertListEqual - sprawdza czy dwie listy są równe
assertTupleEqual - sprawdza czy dwie tuple są równe
assertSetEqual - sprawdza czy dwa zbiory są równe
assertDictEqual - sprawdza czy dwa słowniki są równe
"""

import unittest

class SimpleTest(unittest.TestCase):
    
    def test1(self):
        self.assertListEqual([1, 2, 4], [1, 2, 3])
        
    def test2(self):
        self.assertTupleEqual((1, 3), (1, 2))
        
    def test3(self):
        self.assertSetEqual({4, 2}, {4, 5})
        
    def test4(self):
        self.assertDictEqual({'a': 2, 'b': 2}, {'a': 1, 'b': 2})
        
    
if __name__ == '__main__':
    unittest.main()