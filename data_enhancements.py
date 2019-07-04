# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 19:44:42 2019

@author: Anuj
"""

import pandas as pd
file = 'the-office-lines - scripts.csv'
dataset = pd.read_csv(file, low_memory=False)


dataset = dataset[dataset['deleted'] == False]
dataset['speaker'] = dataset['speaker'].replace('David', 'David Wallace')
dataset.to_csv('the-office-lines - scripts - enhanced.csv', index=False)