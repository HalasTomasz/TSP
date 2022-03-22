import networkx as nx
import matplotlib.pyplot as plt
import tsplib95
import networkx as nx
import functions


def read_graph(file):
    
    with open(file) as f:
        problem = tsplib95.read(f)
        
    #print(len(list(problem.get_edges())))
    Graph = problem.get_graph()
    #print(G.number_of_edges())
    #print(G.number_of_nodes())
    #print(G[1][2]['weight'])
    
    Graph = Graph.to_directed()
    #print(G.number_of_edges())
    #print(G.number_of_nodes())
    
    solution = tsplib95.load_solution('bays29.opt.tour')
    solution = solution.trace_tours('opt.tours')
    print(solution)
    #problem.trace_tours(solution)
    
    return Graph

if __name__ == '__main__':
    Graph = read_graph('bays29.tsp')
    print(Graph.number_of_edges())
    functions.OPT2(Graph)
    
    # functions.k_random(Graph, 5)
    #functions.nearest_neighbour(Graph)


# Graf pełny vs graf skierowany?

