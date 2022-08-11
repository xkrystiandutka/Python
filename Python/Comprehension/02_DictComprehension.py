# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 15:51:54 2022

@author: Krystian
"""

stocks = {'AMZN.US': 'Amazon.com Inc', 'GOOGL.US': 'Alphabet Inc',
          'AAPL.US': 'Apple Inc', 'UBER.US': 'Uber Technologies Inc',
          'MSFT.US': 'Microsoft Corp'}

# %%
stocks.keys()
stocks.values()
stocks.items()

for key, value in stocks.items():
    print('{:8}: {}'.format(key, value))
    
# %%
stocks_dict = {key:value for (key, value) in stocks.items()}

# %%
stocks_set = {(key, value) for (key, value) in stocks.items()}

# %%
stocks_invert = {value:key for (key, value) in stocks.items()}

# %%
stocks_lower = {key.lower():value for (key, value) in stocks.items()}

# %%
stocks_length = {key:len(value) for (key, value) in stocks.items()}

# %%
s_l = {k: v + ':' + str(len(v)) for (k, v) in stocks.items()}


# %%

def replaceCorpInc(name):
    name = name.replace('Corp', '0')
    name = name.replace('INC', '1')
    return name

stocks_flag = {k:replaceCorpInc(v) for (k,v) in stocks.items()}
    
# %%

stockCorp = {key:val for (key,val) in stocks.items() if 'Corp' in val}
stockInc = {key:val for (key,val) in stocks.items() if 'Inc' in val}

# %%
stocksA = {key:val for (key, val) in stocks.items() \
            if val.startswith('A') if len(val) < 13}
    
# %%

dicts = {'jeden': 1, 'dwa': 2, 'trzy': 3}

print({val:key for (key, val) in dicts.items()})