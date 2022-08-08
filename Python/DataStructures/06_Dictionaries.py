# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 10:17:34 2022

@author: Krystian
"""

emptyDict = dict()
print(emptyDict)

d = {}
print(type(d))

e = set()

# %%

polToEng = {'jeden':'one', 'dwa':'two', 'trzy':'three'}

nameToDigit = {'jeden':1, 'dwa':2, 'trzy':3}

# %%

nameToDigit = {0:1, 1:2, 2:3}

len(nameToDigit)

# %%
# dict = {'key1':'value1', 'key2':'value2'}

# %%
polToEng['cztery'] = 'four'

# %%
polToEng.clear()

# %%
polToEngCopied = polToEng.copy()

# %%
list(polToEng.keys())

# %%
list(polToEng.values())

# %%
list(polToEng.items())

# %%
# polToEng['jeden']
# polToEng['zero']

# %%
polToEng.get('zero', 'NaN')

# %%
# polToEng.pop('dwa')
# polToEng.popitem()

# %%
polToEng.update({'dwa':2})

print(polToEng)