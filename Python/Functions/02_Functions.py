# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 17:38:50 2022

@author: Krystian
"""

def funkcja1():
    print('Pierwsza funkcja uruchomiona.')

funkcja1()

# %%
def funkcja2(x=3, y=10):
    print('Podane argumenty to: x={0}, y={1}'.format(x, y))

funkcja2(y=3, x=5)

# %%
import math
math.sqrt(2)
math.exp(1)
math.sin(0)

# %%
def funkcja3():
    print('Uruchomiono.')

funkcja3()
print(type(funkcja3))
funkcja3()

fun = funkcja3()
# %%
def add(x, y):
    return x + y

result = add(2, 6)

# %%
def subtract(x: int, y: int):
    return x - y

subtract(10, 6)

# %%
def print_menu():
    print('Start programu...')
    print('*' * 30)
    print("""Wybierz jedną z podanych opcji:
        0 - logowanie
        1 - wyjscie""")
    print('*' * 30)
    print('Koniec programu.')

print_menu()