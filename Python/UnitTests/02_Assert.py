# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 14:12:28 2022

@author: Krystian
"""

assert 1 == 1

# %% 

#assert 1 == 3

# %%

def testSum():
    assert sum([1,2,3]) == 6, 'Should be 6'
    
def testMin():
    assert min([1, 2, 3]) == 1, 'Should be 1'

# %%
if __name__ == '__main__':
    testSum()
    testMin()
    print('All fine.')