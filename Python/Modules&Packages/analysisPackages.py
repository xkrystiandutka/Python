# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 21:27:28 2022

@author: Krystian
"""


import rocket.data

# %%
dir(rocket.data)

# %%
dane = rocket.data.get_data()

# %%
import rocket.algorithms

# %%
dir(rocket.algorithms)

rocket.algorithms.drzewa_decyzyjne()

# %%
from rocket.algorithms import drzewa_decyzyjne

# %%
drzewa_decyzyjne()

# %%
from rocket.function.stats import mean

# %%
mean(dane)