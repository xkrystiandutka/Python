# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 11:17:01 2022

@author: Krystian
"""

# print(2+2)

print(2 + 2)

print(3 * 3)

3 + 2 * 2
4 - 2 * 2

print(3 + 2 * 2)

10 / 3
4 / 2

10 // 3 

10 % 3

12 % 5 

13 % 2

(5 - 2 **3 ) * 10

x = 10
y = 20

z = x * y

print(z)

print('love python')
print("love python")

"It's the best!"

print('It\'s the best!')

print('Python\n3.9')

print("""
      Python
      3.9
      """)
    
    
print('\tPython')

print('\t\t\tPython')

print('C:\path\\to\something\\new')

print(r'C:\path\to\something\new')
print('C:\\path\\to\\something\\new')

import os
os.getcwd()

# %%

print("""Instrukcja uruchamiania pliku przyklad.py:
    --file [nazwa pliku]
        zapisuje output do pliku
    --quiet
        wycisza logi w konsoli
Koniec.""")

# %% 

text = 'I love Python. '
print(text * 3)
print('hau...' * 8)
print('*' * 30)

# %%

'Python'
'Py' 'thon'
print('Py' 'thon')

# %%
url = 'https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/python_course/python.png'

url_2 = ('https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/'
         'python_course/python.png')
# %%

name = 'Python'

print(name + ' 3.9')
print(name, '3.9')

# %% 

age = 22
name = 'Krystian'

print(name + ' ' + str(age))
print(name, age)
print('{0} ma {1} lat.'.format(name, age))

# %%

saldo = 40
print(saldo)

saldo = saldo + 50
print(saldo)

saldo += 50
print(saldo)

# %%
lokata = 1000
czynnik_akumulacyjny = 1 + 0.04
lokata_po_roku = lokata * czynnik_akumulacyjny
print('Wartosc lokaty po roku:', lokata_po_roku)

# %%
pixel = 150
pixel /= 255
print(pixel)

# %%
base = 2
base **= 5
print(base)

# %%
x = 103
x %= 10
print(x)

# %%
imie = 'Krystian '
nazwisko = 'Dutka'
imie += nazwisko

# %%
name = 'Python '
version = '3.7'
name += version
print(name)
