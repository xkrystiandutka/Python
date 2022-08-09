# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:45:38 2022

@author: Krystian
"""

rawData = '332!25!3225!42224'

cleanData = ''

for char in rawData:
    if char != '!':
        cleanData = cleanData + char
    else:
        cleanData = cleanData + ','
print(cleanData)

# %% 

for char in rawData:
    if char != '!':
        cleanData += char
    else:
        cleanData += ','
print(cleanData)

# %%

suma = 0
for i in range(101):
    suma += i
print(suma)

# %%

saldo = 450
print('Saldo poczatkowe {}'.format(saldo))

for kwota in range(10, 60, 10):
    print('Wyplacona kwota {}'.format(kwota))
    saldo -= kwota
    print('Saldo: {}'.format(saldo))
print('Saldo końcowe: {}'.format(saldo))

# %%

print('Witaj w systemie logowania.')
print('*' * 30)
nick = input('Podaj swój nick: ')
pin = input('Podaj swój kod pin, {}: '.format(nick))

if len(pin) == 4:
    for char in pin:
        if char not in '0123456789':
            print('Podałes niepoprawny kod pin.')
            break
    else:
        print('Kod pin ważny.')
else:
    print('Podałes niepoprawny kod pin.')
