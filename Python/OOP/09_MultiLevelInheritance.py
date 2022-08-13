# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 11:20:46 2022

@author: Krystian
"""

class Person:
    
    derivation = 'Earh'
    # name = 'Krystian'
    

class Pole(Person):
    
    country = 'Poland'
    # name = 'Dominik'
    

class Programmer(Pole):
    
    tech = 'Python'
    name = 'Kamil'
    
    def info(self):
        print(f'Derivation: {self.derivation}\n'
              f'Country: {self.country}\n'
              f'Technologies: {self.tech}\n'
              f'Name: {self.name}')
        
# %%
programmer1 = Programmer()
programmer1.info()