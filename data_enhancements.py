# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:44:42 2019

@author: Anuj
"""

import pandas as pd
import re

file = 'dataset/the-office-lines - scripts.csv'
dataset = pd.read_csv(file, low_memory=False)

# Consider non deleted scenes only
dataset = dataset[dataset['deleted'] == False]

# Merge David and David Wallace
dataset['speaker'] = dataset['speaker'].replace('David', 'David Wallace')

ids = []

# Remove sounds effects/expressions/gestures like [laughing], [birds chirping], [nods]
print('Trying to remove sounds effects/expressions/gestures..')
print('I am using iterrows() to traverse entire dataset which is apparently very slow, pls suggest an faster alternative..')
temp = pd.DataFrame([], columns=[])
for index, row in dataset.iterrows():
    string = row['line_text']
    if row['id']%1000 == 0:
        print(row['id'], ' rows processed out of 60,000...')
    if re.search(r"[\[].*?[\]]", string) != "None":      
        stripped = re.sub(r"[\[].*?[\]]", "", string, flags=re.X)
        stripped = stripped.strip()
        if len(stripped) == 0:
            dataset = dataset.drop(index)
        if len(stripped) > 0:
            row['line_text'] = stripped
            temp = temp.append(row, ignore_index=True)

for index, row in temp.iterrows():
    dataset.loc[dataset.id == row.id, 'line_text'] = row['line_text']
    
# Write enhanced script to csv
dataset.to_csv('dataset/the-office-lines - scripts - enhanced.csv', index=False)