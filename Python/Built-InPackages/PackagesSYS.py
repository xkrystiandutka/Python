# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:50:28 2022

@author: Krystian
"""

import sys

print(sys.argv)

args = sys.argv

print('Nazwa pliku:', args.pop(0))

i = 1
while args:
    print('Argument nr {}: {}'.format(i, args.pop(0)))
    i += 1