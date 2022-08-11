# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:53:35 2022

@author: Krystian
"""

def generator():
    
    yield 4
    yield 5
    
# %%

gen = generator()

next(gen)

# %%

def generator2(word):
    letters = list(word)
    for letter in letters:
        yield letters
        
gen2 = generator2('python')

next(gen2)

# %%
for item in generator2('predator'):
    print(item)
       
# %%
gen = generator2('comp')

# %%

files = ['script_1.py', 'script_2.py', 'text.txt']

def gen_files(lista):
    for item in lista:
        if item.endswith('.py'):
            yield item
            
gen = gen_files(files)

# %%
next(gen)

# %%
for i in gen:
    print(i)

# %%

files = ['run_me.py', 'README.md', 'help.txt.', 'script.py', 'menu.py', 'main.py', 'py']


def generator_py(files):
    for file in files:
        if file.endswith('.py'):
            yield file
            
gen = generator_py (files)

next(gen)