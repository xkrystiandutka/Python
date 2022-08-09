# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:35:51 2022

@author: Krystian
"""

for i in range(10):
    if i == 6:
        continue
    print(i)

# %%
for i in range(20):
    if i % 2 == 0:
        continue
    print(i)

# %%
for i in range(20):
    if i % 2 == 1:
        continue
    print(i)

# %%
sample = 'Python Course'
for char in sample:
    if char == ' ':
        continue
    print(char)

# %%
hashtags = '#summer#holiday#free'
result = ''
for char in hashtags:
    if char == '#':
        print(result)
        result = ''
        continue
    result = result + char
print(result)
