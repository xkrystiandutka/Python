# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 21:19:19 2022

@author: Krystian
"""

def test_args(x, *args):
    print('Pierwszy paramet:', x)
    for arg in args:
        print('Kolejny parametr *args:', arg)

test_args(4, 3, 4, 2, 5)

# %%
def funkcja_1(x, y, *args):
    print('x=', x)
    print('y=', y)
    print('*args=', args)

funkcja_1(1, 2)
funkcja_1(1, 2, 3)
funkcja_1(1, 2, 3, 4)

# %%
def suma(x, y):
    return x + y

def suma_dowol(*args):
    return sum(args)

# %%
# suma(1, 2, 4)
suma_dowol(1, 2, 3, 5, 3, 5, 2)
