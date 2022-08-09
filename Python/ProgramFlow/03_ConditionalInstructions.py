# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 10:01:21 2022

@author: Krystian
"""

print('Program uruchomiony...')
print("""Włam się do systemu, zgadując dwucyfrowy pin.
Numer pin składa się z cyfr: 0, 1, 2.""")
pin = input('Wprowadź numer pin: ')

if pin == '21':
    print('Brawo! Złamałes system.')
elif pin == '20':
    print('Byles blisko!')
else:
    print('Nie zgadłes.')

# %%
pin = int(input('Wprowadź numer pin: '))

if pin == 21:
    print('Brawo! Złamałes system.')
elif pin == 20:
    print('Byles blisko!')
else:
    print('Nie zgadłes.')

# %%
bool('')

# %%
string = ' '

if string:
    print('Niepusty ciąg znaków')
else:
    print('Pusty ciąg znaków')

# %%
number = 12

if number:
    print('Liczba niezerowa!')
else:
    print('Zero')
