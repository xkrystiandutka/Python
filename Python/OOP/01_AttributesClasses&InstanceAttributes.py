# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 13:14:00 2022

@author: Krystian
"""

class Tree:
    
    name = 'Sosna'
    age = 45
    hight = 15
    
tree1 = Tree()
tree2 = Tree()

print(id(tree1))
print(id(tree2))

# %%

dir(tree1)

# %%

tree1.name
tree1.age
tree1.hight

# %%

tree1.state = 'good'

print(dir(tree2))

# %%

Tree.place = 'forest'

print(dir(tree2.place))

# %%
# print(dir(tree2))
# print(tree2.miejsce)

tree2.miejsce = 'park'

print(tree2.miejsce)