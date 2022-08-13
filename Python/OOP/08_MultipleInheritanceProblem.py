# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 11:14:28 2022

@author: Krystian
"""

class A:
    
    def method(self):
        print('Method from class A')
        
class B(A):
    
    pass
        
class C(A):

    pass

class D(B,C):
    
    pass

# %%
d = D()
d.method()     