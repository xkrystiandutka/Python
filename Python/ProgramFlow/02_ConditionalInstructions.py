# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 09:39:17 2022

@author: Krystian
"""

version = 3.9

print(version)

version > 3
version <= 3

# %%

number = 1200

number > 1000
number == 1200

number == 1200
number == 1000

number != 1200
number != 1000

# %%
if 8 > 10:
    print('Tak')

# %%
a = 15
if a > 10:
    print('a > 10')

# %%
a = 5
if a > 10:
    print('a > 10')
else:
    print('a <= 10')

# %%
age = 18

if age < 18:
    print('Nie masz uprawnien.')
else:
    print('Dostęp przyznany.')

# %%
age = 18
if age == 18:
    print('Masz 18 lat.')
elif age < 18:
    print('Nie masz uprawnien.')
else:
    print('Dostep przyznany.')

# %%
age = int(input('Podaj swoj wiek: '))
if age == 18:
    print('Masz 18 lat.')
elif age < 18:
    print('Nie masz uprawnien.')
elif age > 18:
    print('Dostep przyznany.')
