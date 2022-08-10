# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 10:46:17 2022

@author: Krystian
"""


techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'w') as file:
    for tech in techs:
        print(tech, file=file)
        
# %%

evenNumber = list(range(100))[::2]

with open ('numbers.txt', 'w') as file:
    for number in evenNumber:
        file.write(str(number) + '\n')
        
# %%
techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'a') as file:
    for tech in techs:
        print(tech, file=file)
        
# %%
technologies = []
with open('techs.txt', 'r') as file:
    for line in file:
        technologies.append(line)
print(technologies)

# %%
technologies = []
with open('techs.txt', 'r') as file:
    for line in file:
        technologies.append(line[:-1])
print(technologies)


# %%
with open('tree.txt', 'w') as file:
    for j in range(2):
        for i in range(10):
            print('{:>9}'.format('*' * i), end='', file=file)
            print('{}'.format('*' * i), file=file)



