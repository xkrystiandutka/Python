# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:45:40 2022

@author: Krystian
"""

name = 'Python'

# %%

print(name)
print(name[0])
print(name[5])
#print(name[6])
print(name[-1])

# %%

print(name[0:3])
print(name[:2])
print(name[3:])

print(name[-2:])

# %%
full = 'Python Programming'
print(full[7:])
print(full[::2])

# %%
sample = '#stop#this#flow'
print(sample[::5])

# %%
numbers = '8,9,7,4'
print(numbers[::2])

# %%
print(numbers[::-1])

# %%
name = 'kajak'
print(name[::-2])
# %%

name = 'Python'

'Py' in name
'java' in name
