import math
import networkx as nx
import numpy as np
import random
import ast
import copy

"""
 SYM <- symetric graph
 ASYM <- asymetric graph
 FUll <- complete graph
 EU <- euklidian potins
 types = ['sym', 'asym','full' 'eu']
"""
def generate_graph(n, seed, type_of_problem):
    
    new_graph = nx.DiGraph()
    random.seed(10)
    
    if type_of_problem == "sym":

        for i in range(1, n+1):
            for j in range(i + 1, n+1):
        
                weight = random.randrange(1,1000)
                new_graph.add_edge(i, j % (n +1), weight=weight)
                new_graph.add_edge(j, i % (n +1), weight=weight)
                
    elif type_of_problem == "asym":
       
        for i in range(1, n+1):
            for j in range(i + 1, n+1):

                new_graph.add_edge(i, j % (n +1), weight=random.randrange(1,1000))
                new_graph.add_edge(j, i % (n +1), weight=random.randrange(1,1000))
    
    elif type_of_problem == "full":
         tmp = nx.complete_graph(range(1, n +1)) 
         
         for (node1,node2,data) in tmp.edges(data=True):
             #print(node1,node2,data)
             tmp[node1][node2]['weight'] = random.randrange(1,1000)
             
         return tmp
        
    else:
        node_list = []
        for i in range(1, n+1):
             
             x = random.randrange(1,1000)
             y = random.randrange(1,1000)
             node_list.append((i,x,y))
             
        for out_edge in node_list:
            for to_edge in node_list:
            
                if out_edge == to_edge :
                    continue
                number = int(math.sqrt((out_edge[1]-to_edge[1])**2 +(out_edge[2]-to_edge[2])**2))
                new_graph.add_edge(out_edge[0], to_edge[0], weight = number)
    return new_graph

def k_random(graph, k):
    final = 0
    for j in range(0, k):
        
        perm = np.random.permutation(graph)
        #print(perm)
        dist = 0
        for i in range(0, len(perm)):
            dist += graph[perm[i]][perm[(i + 1) % len(perm)]]['weight']
        if final == 0 or dist < final:
            final = dist
            final_perm = perm # Here added line
        #print(dist)
#        print(final)
    return final_perm,final


def nearest_neighbour(graph, source):
    route = [source]
    vertices_left = [value for value in graph.nodes() if value not in route]
    vertex = source

    total = 0
    while vertices_left:
        dist = 0
        for target in vertices_left:
            if dist == 0 or dist > graph[source][target]['weight']:
                dist = graph[source][target]['weight']
                vertex = target
        route.append(vertex)
        vertices_left.remove(vertex)
        # print("source: ", source, ", target: ", vertex, ", distance: ", dist)
        source = vertex
        total += dist

    # print("source: ", source, ", target: ", route[0], ", distance: ", graph[source][route[0]]['weight'])
    total += graph[source][route[0]]['weight']
    return route, total


def extended_nearest_neighbour(graph):
    total = 0
    final_sol = []
    for source in graph.nodes():
        solution = nearest_neighbour(graph, source)
        if total == 0 or solution[1] < total:
            total = solution[1]
            final_sol = solution

    return final_sol[0],final_sol[1]


def OPT2(graph):
    
    #starting_permutation = np.random.permutation(graph.number_of_nodes())
    #starting_permutation = starting_permutation + 1
    
    starting_permutation = list(range(1, graph.number_of_nodes() + 1))
    number_of_nodes = graph.number_of_nodes()

    value = calc_distances(graph, starting_permutation)
    best_path = {str(starting_permutation): value}

    best = min(best_path.items(), key=lambda x: x[1])

    no_new_solution = False
    old_perm = best[0]
    old_best = best[1]
    tmp = []
    while not no_new_solution:

        for i in range(0, number_of_nodes):
            for j in range(i + 1, number_of_nodes):
  
                new_permutation = ast.literal_eval(best[0])
                start = i 
                finish = j
                while start < finish:
                    
                    new_permutation[start], new_permutation[finish] = new_permutation[finish], new_permutation[start]
                    finish = finish - 1
                    start = start + 1

                value = calc_distances(graph, new_permutation)
                tmp.append(value)
                best_path[str(new_permutation)] = value
        
        best = min(best_path.items(), key=lambda x: x[1])
        best_path = {}

        if old_best <= best[1]:
            no_new_solution = True
        else:
            old_perm = best[0]
            old_best = best[1]

    return old_perm, old_best


"""
Not using dic any more
"""
def New_OPT2(graph):
    
    #starting_permutation = np.random.permutation(graph.number_of_nodes())
    #starting_permutation = starting_permutation + 1
    
    starting_permutation = list(range(1, graph.number_of_nodes() + 1))
    number_of_nodes = graph.number_of_nodes()

    no_new_solution = False
    old_perm = list(range(1, graph.number_of_nodes() + 1))
    old_best = calc_distances(graph, starting_permutation)

    while not no_new_solution:

        for i in range(0, number_of_nodes):
            for j in range(i + 1, number_of_nodes):
  
                new_permutation = copy.deepcopy(old_perm)
                start = i 
                finish = j
                while start < finish:
                    
                    new_permutation[start], new_permutation[finish] = new_permutation[finish], new_permutation[start]
                    finish = finish - 1
                    start = start + 1

                value = calc_distances(graph, new_permutation)
                if old_best > value:
                    old_best = value
                    best_path = new_permutation
                    change = True
        if change:
            old_perm = best_path
        else:
            no_new_solution = True
        change = False
            
    return old_perm, old_best


def calc_distances(graph, permutation):
    dis = 0
    for i in range(0, len(permutation)):
       # print(i,len(permutation))
        dis = dis + graph[permutation[i]][permutation[(i + 1) % len(permutation)]]['weight']
    return dis
