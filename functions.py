import math
import networkx as nx
import numpy as np
import random 
import ast

def genrate_graph(n,seed,symetric):
    
    new_graph = nx.Graph()
    random.seed(10)
    for i in range(0,n):
        for j in range(i+1,n):
           new_graph.add_edge(i,j,weight= random.random())
    
    if(not symetric):
        new_graph = new_graph.to_directed()
        


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



def OPT2(Graph):
    
    #starting_permutation = np.random.permutation(Graph.number_of_nodes())
    starting_permutation = list(range(1,Graph.number_of_nodes() +1))
    number_of_nodes = Graph.number_of_nodes()
    
    valuve = caluc_distances(Graph, starting_permutation)
    best_path = {}
    
    best_path[str(starting_permutation)] = valuve
    best = min(best_path.items(), key=lambda x: x[1]) 
    
    no_new_soultion = False
    old_perm = best[0]
    old_best = best[1]
    
    while(not no_new_soultion):
        
        for i in range(0,number_of_nodes):
            for j in range(i+1,number_of_nodes):
                #print(i,j)
                new_permuation = ast.literal_eval(best[0]) 
                new_permuation[i], new_permuation[j] = new_permuation[j], new_permuation[i]
                
                valuve = caluc_distances(Graph, new_permuation)
                
                best_path[str(new_permuation)] = valuve
                
        best_path[str(starting_permutation)] = valuve
        best = min(best_path.items(), key=lambda x: x[1]) 
        #print(best)
        best_path = {}    
        
        if old_best <= best[1]:
            no_new_soultion = True
        else:
            old_perm = best[0]
            old_best = best[1]
            #print(old_perm)
            #print(old_best)
            
    print(old_perm)
    print(old_best)
    
def caluc_distances(Graph,permuation):
    
    dis = 0
    for i in range(0,len(permuation) -1):
        dis = dis + Graph[permuation[i]][permuation[i+1]]['weight']
    return dis