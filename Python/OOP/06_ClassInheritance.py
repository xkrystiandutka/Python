# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 06:26:15 2022

@author: Krystian
"""

class Person:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def info(self):
        print(f'{self.name} {self.surname}')
      
        
class Footballer(Person):
    
    def __init__(self, name, surname, club):
        super().__init__(name, surname)
        self.club = club
        
    def info(self):
        super().info()
        print(f'Klub: {self.club}')
        
# %%
footballer1 = Footballer('Robert', 'Lewandowski', 'Bayern') 
footballer2 = Footballer('Krzysztof', 'Piątek', 'AC Milan')

# %%

footballer1.info() 
footballer2.info() 