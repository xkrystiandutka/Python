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

# %%

def print_even(maximum):
    even = []
    for i in range(maximum + 1):
        if i % 2 == 0:
            even.append(i)
    return even
            
print_even(10)
num = print_even(20)

# %%

def write_file(file_name, text):
    with open(file_name, 'w') as file:
        print(text, file=file)
        
write_file('sample.txt', 'Pierwsza linbia.\nDruga linia.')
write_file('sample2.txt', 'Pierwsza.\nDruga.\nTrzecia.')

# %%

def calculate_profit(pv,rate,n):
    return pv * (1+rate)**n - pv

profit = calculate_profit(1020, 0.02, 1)

realProfit = profit * 0.81

print(profit)
print(realProfit)

# %%

def drukuj_nieparzyste(x):
    odd = []
    for i in range(20):
        if i % 2 == 1:
            odd.append(i)
    return odd
            
drukuj_nieparzyste(20)