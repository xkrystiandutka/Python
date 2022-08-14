# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:07:30 2022

@author: Krystian
"""

def add(x, y):
    """Zwraca sumę dwóch liczb.
    """
    return x + y


if __name__ == '__main__':
    import doctest
    doctest.testfile('test.txt')
