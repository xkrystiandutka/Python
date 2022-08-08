# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:35:55 2022

@author: Krystian
"""

emptyTuple = tuple()
print(emptyTuple)

# %%

amazon = ('Amazon', 'USA', 'Technology', 1)

google = ('Google', 'USA', 'Technology', 2)

print(google[1])

# %%

data = (amazon, google)

print(data)

# %%

a = ('Krystian', 'Dutka')
print(a)

# %%

name = 'Krystina'
surname = 'Dutka'

name, surname, idUser = ('Krystian', 'Dutka', '0001')

# %%

amazonName, country, sector, rank = amazon

# %%
stocks = 'Amazon', 'Apple', 'IBM'

print(type(stocks))

# %%
nested = 'Europa', 'Polska', ('Warszawa', 'Krakow', 'Wroclaw')
print(nested)

# %%
a = 12
b = 14

c = b
b = a
a = c
print(a, b)

# %%
x, y = 10, 15

x, y = y, x
print(x, y)
