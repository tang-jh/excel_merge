# Import libraries
import os
import numpy as np
import pandas as pd
import string

# Function to generate demo folder tree and files
def generate_rand_df():
    names = []
    scores_1 = []
    scores_2 = []
    data = []
    for n in range(20):
        names.append(''.join(np.random.choice(list(string.ascii_letters), size=8)))
        scores_1.append(np.random.randint(1,10))
        scores_2.append(np.random.randint(1,10))
    data = list(zip(names,scores_1,scores_2))
    return pd.DataFrame(data, columns = ['Name', 'Score_1', 'Score_2'])

# Function to generate dummy data with specified folder tree
def folder_str(subdir_one, subdir_two, files, root_path="proj_root"):
    ''' 
    files = number of files within each second level subfolders
    subdir_one = number of first level subfolders
    subdir_two = number of second level subfolders
    root_path = path name of root folder
    '''
    new_paths = []
    for i in range(subdir_one):
        for j in range(subdir_two):
            new_paths.append("{}/folder{}/subfolder{}".format(root_path,i,j))
            for n in new_paths:
                os.makedirs(n, mode=777, exist_ok=True)
                for k in range(files):
                    generate_rand_df().to_excel('{}/file{}.xlsx'.format(n, k), index=False)

# Generate the dummy folder tree
# folder_str(2, 2, 2)

