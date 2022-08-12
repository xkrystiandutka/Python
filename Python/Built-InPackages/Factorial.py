# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:03:02 2022

@author: Krystian
"""

import sys


def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)


if __name__ == '__main__':
    print(silnia(int(sys.argv[1])))