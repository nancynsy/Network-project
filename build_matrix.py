import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import networkx as nx
import csv

for n in range(98,111,1):
    df = pd.read_csv('{}congress.csv'.format(n))
    
    RESULT = (df["Senator"]).tolist()
    with open("{}_names.txt".format(n),'w') as resultFile:
        for item in RESULT:
            resultFile.write('{} \n'.format(item))
    
    
    RESULT = (df["Election Data"]).tolist()
    with open("{}_election_data.csv".format(n),'w') as resultFile:
        for item in RESULT:
            resultFile.write('{} \n'.format(item))
    
    RESULT = (df["win/lose"]).tolist()
    with open("{}_win_lose_data.csv".format(n),'w') as resultFile:
        for item in RESULT:
            resultFile.write('{} \n'.format(item))
            
    icpsr_ids = (df["ICPSR ID"])
    np.savetxt(
        'identifying_info_{}.csv'.format(n),           # file name
        icpsr_ids,                # array to save
        fmt='%d',             # formatting, 2 digits in this case
        delimiter=',',          # column delimiter
        newline='\n')        # new line character
    
    party_affiliation = (df["Party"])
    np.savetxt(
        'party_info_{}.csv'.format(n),           # file name
        party_affiliation,                # array to save
        fmt='%d',             # formatting, 2 digits in this case
        delimiter=',',          # column delimiter
        newline='\n')        # new line character
    
    dfsub=df.iloc[:,4:]
    dfs = scipy.sparse.csr_matrix(dfsub.values)
    
    rows, columns = dfs.get_shape()
    adjacency_matrix = np.zeros((rows,rows))
    for j in range(1,columns,1):
        non_zero_row, position = dfs[:,j].nonzero()
        for element in non_zero_row:
            if dfs[element,j] == 1:
                the_one = element 
                break
        for element in non_zero_row:
            
            #if dfs[element,0] != dfs[the_one,0]:
                if dfs[element,j] == 2:
                    adjacency_matrix[element, the_one] += 1

    for i in range(len(adjacency_matrix)):
        adjacency_matrix[i,i] = 0
    
    print(adjacency_matrix)
    
    np.savetxt(
        'adjacency_matrix_non{}.csv'.format(n),           # file name
        adjacency_matrix,                # array to save
        fmt='%d',             # formatting, 2 digits in this case
        delimiter=',',          # column delimiter
        newline='\n')        # new line character

        
