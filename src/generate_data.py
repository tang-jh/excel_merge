'''
Module to generate a demo folder structure for testing purpose.
This demo takes the structure of individual Excel files based on an assessor of the test candidate.
Each candidate is assigned 3 assessors and will be assessed on 3 criteria
'''

# Import libraries
import os
import numpy as np
import pandas as pd

# Function to generate a list of unique running ID
def generate_ids(prefix="ID", suffix="", num=480):
    ids = []
    for i in range(num):
        ids.append('{}{}{}'.format(prefix, str(i).zfill(5), suffix))
    return ids

# Generate an allocation table of assessor to candidate
cohort = generate_ids()
assessor = generate_ids(prefix="Ax", suffix="N", num=50)
asc_1 = []
asc_2 = []
asc_3 = []
for c in cohort:
    first, second, third = (np.random.choice(assessor) for i in range(3))
    while second == first:
        second = np.random.choice(assessor)
    while third == second or third == first:
        third = np.random.choice(assessor)
    asc_1.append(first)
    asc_2.append(second)
    asc_3.append(third)
    
data = list(zip(cohort, asc_1, asc_2, asc_3))
df_allocation = pd.DataFrame(data, columns=['Candidate','Asc1','Asc2','Asc3'])

# Creates a 2>>4 folder structure and randomly allocate assessors dataframe as Excel file
subdir_1 = ['Group_1', 'Group_2']
subdir_2 = ['Section_1', 'Section_2', 'Section_3', 'Section_4']
new_paths = []
for i in subdir_1:
    for j in subdir_2:
        new_paths.append('proj_root/{}/{}/'.format(i,j))
        for n in new_paths:
            os.makedirs(n, mode=777, exist_ok=True)
            
# Generate collection of dataframes based on assessors with random scores and randomly allocate to subfolders
asc_total = np.unique(asc_1 + asc_2 + asc_3) #ensure all unique assessors included
frames = []
for a in asc_total:
    ids_cnd = []
    score_1 = []
    score_2 = []
    score_3 = []
    data = []
    candidates = []
    candidates = df_allocation['Candidate'][(df_allocation['Asc1']==a)|(df_allocation['Asc2']==a)|(df_allocation['Asc3']==a)]
    for c in candidates:
        ids_cnd.append(c)
        score_1.append(np.random.randint(1,10))
        score_2.append(np.random.randint(1,10))
        score_3.append(np.random.randint(1,10))
    data_a = list(zip(ids_cnd,score_1,score_2,score_3))
    df = pd.DataFrame(data_a, columns=['Candidates', 'Criterion_1', 'Criterion_2', 'Criterion_3'])
    frames.append(df)
    df.to_excel('{}{}.xlsx'.format(np.random.choice(new_paths), a), index=False)