import math
import networkx as nx
import numpy as np
import random 

def generate_corr_graph(corr):
    
    for first_el in corr:
        
        for second_el in corr:
            pass
            
            if first_el == second_el:
                continue
            #print(first_el,second_el)
           # print(first_el[0],second_el[0])         
            print(first_el[0],second_el[0],math.sqrt((float(first_el[1]) - float(second_el[1]))**2 + (float(first_el[2]) - float(second_el[2]))**2))
                    

def genrate_graph(n,min_number,max_number):
    
    new_graph = nx.complete_graph(n)
    
    for i in range(0,n):
        for j in range(0,n):
           new_graph[i][j]['weight'] = random.randrange(min_number,max_number)


def k_random(graph, k):
    final = 0
    for j in range(0, k):
        perm = np.random.permutation(graph)
        print(perm)
        sum = 0
        for i in range(0, len(perm)):
            sum += graph[perm[i]][perm[(i+1) % len(perm)]]['weight']
        if sum < final:
            final = sum
    print(sum)

def nearest_neighbour(graph):
    source = 0
    has_been = [0]
    vertices_left = [value for value in graph.nodes() if value not in has_been]

    min = 0
    vertex = 0
    for edge in vertices_left:
        if min == 0 or min > graph[edge[0]][edge[1]]['weight']:
            min = graph[edge[0]][edge[1]]['weight']
            vertex = edge[1]
    has_been.append(vertex)


