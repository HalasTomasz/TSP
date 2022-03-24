import math
import networkx as nx
import numpy as np
import random
import ast


def generate_graph(n, seed, symmetric):
    new_graph = nx.Graph()
    random.seed(10)
    for i in range(0, n):
        for j in range(i + 1, n):
            new_graph.add_edge(i, j, weight=random.random())

    if not symmetric:
        new_graph = new_graph.to_directed()


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
        #print(dist)
    return final


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
    return [route, total]


def extended_nearest_neighbour(graph):
    total = 0
    final_sol = []
    for source in graph.nodes():
        solution = nearest_neighbour(graph, source)
        if total == 0 or solution[1] < total:
            total = solution[1]
            final_sol = solution
    return final_sol


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

    while not no_new_solution:

        for i in range(0, number_of_nodes):
            for j in range(i + 1, number_of_nodes):
                # print(i,j)
                new_permutation = ast.literal_eval(best[0])
                
                start = i 
                finish = j
                while start < finish:
                    new_permutation[start], new_permutation[finish] = new_permutation[finish], new_permutation[start]
                    
                    finish = finish - 1
                    start = start + 1
                #new_permutation[i], new_permutation[j] = new_permutation[j], new_permutation[i]
                
                

                value = calc_distances(graph, new_permutation)

                best_path[str(new_permutation)] = value

        best_path[str(starting_permutation)] = value
        best = min(best_path.items(), key=lambda x: x[1])
        # print(best)
        best_path = {}

        if old_best <= best[1]:
            no_new_solution = True
        else:
            old_perm = best[0]
            old_best = best[1]
            # print(old_perm)
            # print(old_best)

    print(old_perm)
    print(old_best)


def calc_distances(graph, permutation):
    dis = 0
    for i in range(0, len(permutation)):
        dis = dis + graph[permutation[i]][permutation[(i + 1) % len(permutation)]]['weight']
    return dis
