# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 12:16:25 2022

@author: Krystian
"""

i = 0
while i < 5:
    print(i)
    i += 1
    
    
# %%

n = 0
while True:
    print(n)
    if n > 10:
        break
    n += 1
    
# %%

while True:
    name = input('Write your name: ')
    if len(name) >= 3 and name.isalpha():
        break
    print('Hello {}'.format(name))    
    
 

# %%
n = 0

while n < 20:
    n = n + 1
    if n % 2 != 0:
        continue
    print(n)

# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
falga = False

idx = 0
while idx < len(lista_do_przeszukania):
    print(lista_do_przeszukania[idx])
    idx += 1

# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 63

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if flaga:
    print('Znaleziono element {}'.format(wartosc))


# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 60

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if not flaga:
    lista_do_przeszukania.append(wartosc)

# %%

numbers = [23, 12, 53, 13, 65, 1, 45]
flaga = False
wartosc = 135

idx = 0
while idx < len(numbers):
    if numbers[idx] == wartosc:
        flaga = True
        print('essa')
        break
    
print('cvhusa')
