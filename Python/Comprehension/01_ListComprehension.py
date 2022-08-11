# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 15:06:10 2022

@author: Krystian
"""

results = []

for i in range (100):
    results.append(i**2)
print(results)

# %%

results2 = [i**2 for i in range(100)]

# %%

lista = [i * 3 for i in range(100)]

# %%


results3 = []

for i in range (100):
    if i % 5 == 0:
        results3.append(i**2)
print(results3)

# %%

results3 = [i ** 2 for i in range(100) if i % 5 == 0]

print(results3)

# %%

letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']

results4 = []

for letter in letters:
    for number in numbers:
        results4.append(letter + number)

# %%

results4 = [letter + number for letter in letters for number in numbers]

# %%
ls_1 = ['a', 'b', 'c']
ls_2 = ['a', 'b', 'c']

results = [l_1 + l_2 for l_1 in ls_1 for l_2 in ls_2 if l_1 != l_2]

# %%
[[j for j in range(10)] for i in range(5)]

# %%
[[(i, j) for j in range(10)] for i in range(3)]
# %%
[[i * j for j in range(10)] for i in range(10)]

# %%
[[l1 + l2 for l2 in 'abcde'] for l1 in '12345']

# %%
def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)

[silnia(i) for i in range(10)]


