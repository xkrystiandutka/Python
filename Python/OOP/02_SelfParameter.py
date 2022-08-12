# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 13:25:54 2022

@author: Krystian
"""

class Tree:
    
    def showInfoTree(self):
        self.name = 'Pine'
        self.age = 30
        print(f'Tree {self.name} is {self.age} years old.')

tree = Tree()

# %%
tree.showInfoTree()

# %%
Tree.showInfoTree(tree)