# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:26:55 2022

@author: Krystian
"""

def parabola(x):
    return x**2 + 3 

print(type(parabola(30)))

print(parabola(30))

# %%

fun1 = parabola

print(fun1(30))

# %%

l = lambda x: x**2 + 3
l(30)