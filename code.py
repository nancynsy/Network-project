# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 21:01:20 2016

@author: nancynan
"""
import numpy 
import pandas as pd
#import scipy
import matplotlib.pyplot as plt
import networkx as nx
#import csv
from scipy.stats import linregress

mat= pd.read_csv("adjacency_matrix_non98.csv",header=None)
ele= pd.read_csv("98_election_data.csv",header=None)
#mat[mat<4]=0
#del mat['2.5']
#ele2 = ele[numpy.isfinite(ele['0'])]
#ele2=ele.dropna() 
ele2=list(ele.values)
numpy.nan_to_num(ele2)

ele.columns = ['ColA']
ele3 = ele[ele.ColA.notnull()]
mat1=mat.as_matrix(columns=None)
ele1=ele.fillna(value=0) 
ele4=ele.replace(numpy.nan, 0, regex=True)
#mat2=np.delete(mat1, mat1[1:100], axis=1)
mat2 = numpy.matrix(mat1)
graph=nx.DiGraph(data=mat2)
G=nx.from_numpy_matrix(mat2)
def draw():
    pos = nx.circular_layout(G)
    nx.draw_circular(G)
    labels = {i : i + 1 for i in G.nodes()}
    nx.draw_networkx_labels(G,pos, labels, font_size=15)
    plt.show()
betweenness = nx.betweenness_centrality(graph)
degree_centrality = nx.degree_centrality(graph)
closeness_centrality = nx.closeness_centrality(graph)
clo= list(closeness_centrality.values())
deg=list(degree_centrality.values())
bet=list(betweenness.values())


names = []
with open('98_names.txt','r') as input_file:
    for line in input_file: 
        names.append(line[:-3])
election_data = []
with open('98_election_data.csv','r') as input_file:
    for line in input_file: 
        election_data.append(line[:-2])   

for i in range(len(names)):
    nx.set_node_attributes(graph,'names',{i: names[i]})
#    nx.set_node_attributes(graph,'icpsr_ids',{i: icpsr_ids[i]})
#    nx.set_node_attributes(graph,'party',{i: party_ids[i]})
    nx.set_node_attributes(graph,'election_data',{i: election_data[i]})
    nx.set_node_attributes(graph,'betweenness_centrality',{i: betweenness[i]})
    nx.set_node_attributes(graph,'degree_centrality',{i: degree_centrality[i]})
    nx.set_node_attributes(graph,'closeness_centrality',{i: closeness_centrality[i]})

nodes = []
attributes= []
for i in range(len(names)):
    node_number,attribute = graph.nodes(data=True)[i]
    nodes.append(node_number)
    attributes.append(attribute)
    
attributes_no_NaN = []
nodes_no_NaN = []
betweenness_no_NaN = []
degree_no_NaN = []
closeness_no_NaN = []
election_data_no_NaN = []

for i in range(len(names)):
    if attributes[i]['election_data'] != 'nan':
        nodes_no_NaN.append(i)
        attributes_no_NaN.append(attributes[i])
        betweenness_no_NaN.append(attributes[i]['betweenness_centrality'])
        degree_no_NaN.append(attributes[i]['degree_centrality'])
        closeness_no_NaN.append(attributes[i]['closeness_centrality'])
        election_data_no_NaN.append(float(attributes[i]['election_data']))
   
#y = [s for s in ele2 if ele2 ! = nan]

plt.plot(closeness_no_NaN,election_data_no_NaN,'o')

p31 = numpy.asarray(mat1)
za = (p31 <3).sum()
a1=linregress(closeness_no_NaN,election_data_no_NaN)
print (a1)
a2=linregress(betweenness_no_NaN,election_data_no_NaN)
print (a2)
a3=linregress(degree_no_NaN,election_data_no_NaN)
print (a3)