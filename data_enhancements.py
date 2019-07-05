# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:44:42 2019

@author: Anuj
"""

import pandas as pd
import re

file = 'the-office-lines - scripts.csv'
dataset = pd.read_csv(file, low_memory=False)

# Consider non deleted scenes only
dataset = dataset[dataset['deleted'] == False]

# Merge David and David Wallace
dataset['speaker'] = dataset['speaker'].replace('David', 'David Wallace')


# Remove sounds effects/expressions/gestures like [laughing], [birds chirping], [nods]
temp = pd.DataFrame([], columns=[])
for index, row in dataset.iterrows():
    if row['line_text'][0] == '[' and row['line_text'][len(row['line_text'])-1] == ']':
        string = row['line_text']
        stripped = re.sub(r"[\[].*?[\]]", "", string, flags=re.X)
        stripped = stripped.strip()
        if len(stripped) > 0:
            row['line_text'] = stripped
            temp = temp.append(row, ignore_index=True)

for index, row in temp.iterrows():
    dataset.loc[dataset.id == row.id, 'line_text'] = row['line_text']
    
# Write enhanced script to csv
dataset.to_csv('the-office-lines - scripts - enhanced.csv', index=False)