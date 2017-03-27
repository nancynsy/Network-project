# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 11:18:40 2016

@author: nancynan
"""

import numpy as np
import scipy.stats as ss
import networkx as nx
import matplotlib.pyplot as plt
#matplotlib inline
n=98
adjacency_matrix = np.genfromtxt(
    'adjacency_matrix_{}.csv'.format(n),           # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=',',          # column delimiter
    dtype='int')

icpsr_ids = np.genfromtxt(
    'identifying_info_{}.csv'.format(n),           # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=',',          # column delimiter
    dtype='int')

party_ids = np.genfromtxt(
    'party_info_{}.csv'.format(n),           # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=',',          # column delimiter
    dtype='int')

win_lose_data = np.genfromtxt(
    '{}_win_lose_data.csv'.format(n),           # file name
    skip_header=0,          # lines to skip at the top
    skip_footer=0,          # lines to skip at the bottom
    delimiter=',',          # column delimiter
    dtype='str')


names = []
with open('{}_names.txt'.format(n),'r') as input_file:
    for line in input_file: 
        names.append(line[:-3])

election_data = []
with open('{}_election_data.csv'.format(n),'r') as input_file:
    for line in input_file: 
        election_data.append(line[:-2])


graph = nx.from_numpy_matrix(adjacency_matrix,create_using=nx.MultiDiGraph())
nx.info(graph)


betweenness = nx.betweenness_centrality(graph)
degree_centrality = nx.degree_centrality(graph)
closeness_centrality = nx.closeness_centrality(graph)
for i in range(len(names)):
    nx.set_node_attributes(graph,'names',{i: names[i]})
    nx.set_node_attributes(graph,'icpsr_ids',{i: icpsr_ids[i]})
    nx.set_node_attributes(graph,'party',{i: party_ids[i]})
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

    
#selecting for attributes with election data
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
        