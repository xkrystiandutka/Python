# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 16:04:13 2022

@author: Krystian
"""

text = 'Witaj na kursie Pythona.\nPython jest wspaniały.'

print(text)

# %%
dir(text)
help(str.count)

# %%

print(text.capitalize())

print(text.title())

print(text.count('Python'))

print(text.startswith('Witaj'))

print(text.endswith('y.'))

# %%
print('sample.txt'.endswith('.py'))

# %%
print('sample.png'.endswith('.png'))

# %%

print(text.find('Python'))
print(text[text.find('Python'):])

# %%
hashtags = 'sport#gym'
idx = hashtags.find('#')
hashtags[:idx]

# %%
'krystian2526'.isalnum()

# %%
'43434fvd'.isdigit()

# %%
'pyThon'.islower()

'KRYSTIAN'.isupper()

# %%
' '.join(['python', '3.9'])
'#'.join(['sport', 'gym', 'fit'])
','.join(['1', '2', '3', '4'])

# %%
'#good#time#mood'.replace('#', ' ')

# %%
'column name'.replace(' ', '_')

# %%
'    python   '.strip()
'    python   '.lstrip()
'    python   '.rstrip()

# %%
'1,2,3,4,5'.split(',')

'python java php sql sas'.split()

'#gym#fit#mood'.split('#')

# %%
'12'.zfill(5)
'1'.zfill(10)