# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:40:55 2022

@author: Krystian
"""

import os

dir(os)

# %%
os.getcwd()

# %%

os.chdir('..')

# %%
os.getcwd()

# %%

os.system('mkdir test')
# os.rmdir('dir3')
# %%
os.listdir()

# %%
for item in os.listdir():
    print(item)

# %%
for item in os.listdir():
    if item.endswith('.py'):
        print(item)

# %%
for root, dirs, files in os.walk(os.getcwd()):
    print(root)
    print(dirs)
    print(files)

# %%
os.path.join(r'home\user\bin', 'python')