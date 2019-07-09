# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 18:00:00 2019

@author: Anuj
"""
"""
Dataset used: 
https://data.world/abhinavr8/the-office-scripts-dataset
 
The above dataset has been enhanced:
    
1. Speakers 'David' and 'David Wallace' has been merged to 'David Wallace'

2. All deleted scenes/dialogues have not been considered

Enhancement code can be found in data_enhancements.py
"""
###############################################################
# Read data


import pandas as pd
file = 'dataset/the-office-lines - scripts - enhanced.csv'
dataset = pd.read_csv(file, low_memory=False)

###############################################################
# Run analysis only for following characters

characters_include= ['Michael', 
                     'Dwight', 
                     'Jim', 
                     'Pam', 
                     'Andy', 
                     'Kevin',
                     'Angela',
                     'Erin',
                     'Oscar',
                     'Ryan',
                     'Darryl',
                     'Phyllis',
                     'Kelly',
                     'Jan',
                     'Toby',
                     'Stanley',
                     'Meredith',
                     'Holly',
                     'Nellie',
                     'David Wallace',
                     'Gabe',
                     'Creed',
                     'Robert',
                     'Karen',
                     'Clark',
                     'Roy']

dataset = dataset[dataset['speaker'].isin(characters_include)]

#########################################################################
# Calculate all season dialogues count for each character
print('Calulcating dialogue count for each character (all seasons)..')

data = dataset.sort_values('speaker')

data_grouped = data.groupby('speaker')
groups = list(data_grouped.groups.keys())

dialogues_count = pd.DataFrame([], columns=[])

for speaker in groups:
    data_current = data_grouped.get_group(speaker)
    dialogues_count = dialogues_count.append({'speaker': speaker, 'count': int(len(data_current))},ignore_index=True)

dialogues_count = dialogues_count.sort_values(by='count', ascending=False)
dialogues_count.to_csv('results/dialogues_count.csv',index=False) 

#########################################################################
# Calculate season-wise dialogues count for each character
print('Calulcating dialogue count for each character (season wise)..')

data = dataset.sort_values('season')
data_grouped = data.groupby(['season', 'speaker'])
groups = list(data_grouped.groups.keys())

dialogues_count_seasonwise = pd.DataFrame([], columns=[])
for season, speaker in groups:
    data_current = data_grouped.get_group((season, speaker))
    dialogues_count_seasonwise = dialogues_count_seasonwise.append({'season': season, 'speaker': speaker, 'count': int(len(data_current))},ignore_index=True)
    
dialogues_count_seasonwise = dialogues_count_seasonwise.sort_values(by=['season','count'], ascending=False)  
dialogues_count_seasonwise.to_csv('results/dialogues_count_seasonwise.csv', index=False)


data_grouped = dialogues_count_seasonwise.groupby('season')
groups = list(data_grouped.groups.keys())
dialogues_count_seasonwise_top6 = pd.DataFrame([], columns=[])
for season in groups:
#    dialogues_count_seasonwise_top6_separate = pd.DataFrame([], columns=[])
    data_current_top6 = data_grouped.get_group(season).sort_values('count', ascending=False)[:6]
    dialogues_count_seasonwise_top6 = dialogues_count_seasonwise_top6.append(data_current_top6)
#    dialogues_count_seasonwise_top6_separate = dialogues_count_seasonwise_top6_separate.append(data_current_top6)
#    dialogues_count_seasonwise_top6_separate.to_csv('results/dialogues_count_seasonwise_top6_'+ str(int(season)) + '.csv', index=True)

dialogues_count_seasonwise_top6.to_csv('results/dialogues_count_seasonwise_top6.csv', index=True)

########################################################################

print('Finish!')