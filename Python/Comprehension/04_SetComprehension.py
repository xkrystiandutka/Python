# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 20:50:55 2022

@author: Krystian
"""

# %%
text = 'Python jest wspaniały. Python jest elastyczny. Python rządzi.'

words = text.lower().replace('.', '').split()

unique_words = {word for word in words}
print(unique_words)

# %%
unique_words_gt_4 = {word for word in words if len(word) > 4}
print(unique_words_gt_4)

# %%
{word.capitalize() if word.startswith('py') else word for word in words}

# %% 

text = 'python jest popularny w uczeniu maszynowym'

text = list(text)

unique_letter = {letter for letter in text}

print(len(unique_letter))

print(len({letter for letter in text}))