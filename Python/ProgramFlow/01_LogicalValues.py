# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 09:30:55 2022

@author: Krystian
"""

val1 = True
val2 = False

print(val1)
print(type(val2))

# %%

True and True
True and False
False and True
False and False

True or True
True or False
False or True
False or False

True
not True
False
not False

# %%

bool('')
bool('0.0')
bool({})
bool(set())
bool(list())
bool(tuple())

bool({'key':'val'})

