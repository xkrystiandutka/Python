# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 13:29:37 2022

@author: Krystian
"""

import numpy as np

class SquareFunction:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def makeFunction(self):
        print(f'{self.a} * x ** 2 + {self.b} * x + {self.c}')
    
    def solution(self):
        if self.a == 0 and self.b == 0 and self.c == 0:
            print('Identity equation.')
        elif self.a == 0 and self.b == 0 and self.c != 0:
            print('Conflicting equation.')
        elif self.a == 0 and self.b != 0:
            x = - self.c / self.b
            x = round(x, 2)
            print(x)
        elif self.a != 0:
            delta = self.b ** 2 - 4 * self.a * self.c
            if delta > 0:
                sqrt_delta = np.sqrt(delta)
                x1 = (-self.b - sqrt_delta) / (2 * self.a)
                x2 = (-self.b + sqrt_delta) / (2 * self.a)
                x1 = round(x1, 2)
                x2 = round(x2, 2)
                print(x1, x2)
            elif delta == 0:
                x = - self.b / (2 * self.a)
                x = round(x, 2)
                print(x)
            else:
                print('No solutions.')
        else:
            raise Error
        
        
# %%
fk = SquareFunction(3, 1, -4)
fk.makeFunction()
# %%
fk.solution()

# %%
def main():
    for i in range(10000):
        a = np.random.choice(range(-100, 100))
        b = np.random.choice(range(-100, 100))
        c = np.random.choice(range(-100, 100))
        fun = SquareFunction(a, b, c)
        fun.solution()
        
if __name__ == '__main__':
    main()
        