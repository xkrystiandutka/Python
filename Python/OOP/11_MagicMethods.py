# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 11:35:36 2022

@author: Krystian
"""

# %%
1 + 1

# %%
type(1)

# %%
dir(int)

# %%
int.__add__(1, 2)

# %%
int.__sub__(10, 7)

# %%
"""
Operatory:
    +  : __add__(self, other)
    -  : __sub__(self, other)
    *  : __mul__(self, other)
    /  : __truediv__(self, other)
    // : __floordiv__(self, other)
    %  : __mod__(self, other)
    ** : __pow__(self, other)
Operatory Porównawcze:
    <  : __lt__(self, other)
    >  : __gt__(self, other)
    <= : __le__(self, other)
    >= : __ge__(self, other)
    == : __eq__(self, other)
    != : __ne__(self, other)
"""
int.__lt__(3, 6)

# %%

class SpecialInt(int):
    
    def __init__(self, special_int):
        self.special_int = special_int
        
    def __add__(self, other):
        return self.special_int + other.special_int + 10
    
    def __sub__(self, other):
        return self.special_int - other.special_int - 10
     
# %%
s_1 = SpecialInt(2)
s_2 = SpecialInt(3)

s_1 + s_2

# %%
s_1 - s_2

# %%
class Square:
    
    def __init__(self, sideLength):
        self.sideLength = sideLength
        
    def __str__(self):
        return f"Square with side {self.sideLength}cm."
    
    def area(self):
        return self.sideLength ** 2
    
    def __add__(self, other):
        return self.area() + other.area()
    
    def __sub__(self, other):
        return self.area() - other.area()
    
    def __lt__(self, other):
        return self.area() < other.area()
        
# %%
k1 = Square(5)
k2 = Square(10)

# %%
k1.area()

# %%
print(k1)
print(k2)

# %%
k1 + k2

# %%
k1 - k2

# %%
k1 < k2

# %%

