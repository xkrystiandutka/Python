# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:12:21 2022

@author: Krystian
"""

for i in '0123456789':
    i = int(i)
    if i == 6:
        print(i)
        break
    
# %%


for i in '0123456789':
    i = int(i)
    print(i)
    if i == 6:
        break
print('Koniec')

# %%
sample = 'Python Course'
for char in sample:
    if char == ' ':
        break
    print(char)

print('Koniec')

# %%
for char in 'kowalskijgmail.com':
    if char == '@':
        print('Adres email zweryfikowany.')
        break
else:
    print('Adres email nie jest poprawny')


print('Koniec')

