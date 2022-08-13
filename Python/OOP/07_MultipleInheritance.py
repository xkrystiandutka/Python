# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 06:35:37 2022

@author: Krystian
"""

class Person:
      
    origin = 'Earth'
    name = 'Krystian'
    

class Pole:
    
    country = 'Poland'
    # name = 'Oskar'
    
    
class Footballer(Pole, Person):
    
    def info(self):
        print(f'The object created is from the planet {self.origin}.\n'
              f'Country of origin: {self.country}.\n'
              f'Object name: {self.name}')
        
# %%
footballer1 = Footballer()
footballer2 = Footballer()
