# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 13:31:57 2022

@author: Krystian
"""


class Tree:
    
    def __init__(self, name, age, hight):
        self.name = name
        self.age = age
        self.hight = hight
    def isProtected(self):
        if self.age >= 20 and self.hight >= 20:
            print(f'Tree {self.name} is protected.')
        else:
            print(f'Tree {self.name} is not protected.')

    def oneYearMore(self):
        self.age += 1
    
tree1 = Tree('Pine', 35, 25)
tree2 = Tree('Birch', 12, 11)

# %%
print(tree1.name)
print(tree2.name)

# %%
tree1.isProtected()
tree2.isProtected()

# %%
print(tree1.age)
tree1.oneYearMore()
print(tree1.age)
