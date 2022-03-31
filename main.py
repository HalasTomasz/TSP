import tsplib95
import testing_moudle
import functions
import networkx as nx
import time

results = []


def read_graph(file):
    with open(file) as f:
        problem = tsplib95.read(f)

    # print(len(list(problem.get_edges())))
    new_graph = problem.get_graph()
    # print(new_graph.number_of_edges())
    # print(new_graph.number_of_nodes())
    # print(new_graph[1][2]['weight'])

    new_graph = new_graph.to_directed()
    # print(new_graph.number_of_edges())
    # print(new_graph.number_of_nodes())

    opt = tsplib95.load('bays29.opt.tour')
    print(opt)
    print(problem.trace_tours(opt.tours))

    return new_graph


def start_test(path):
    testing_moudle.test(path)


def my_testes():
    testing_moudle.test_auto_generate()


if __name__ == '__main__':
   
    #start_test("C:/Users/denev/TSP/Data_Meta")
    """
    give path to folder with Data
    """

    my_testes()
    """
    generated graph
    """

    # graph = read_graph('bays29.tsp')
    # start = time.time()
    # permutation, solution = functions.opt2(graph)
    # end = time.time()
    # print(end - start)
    # print(permutation)
    # print(solution)

# print(functions.k_random(graph, 2000))
# print(functions.nearest_neighbour(graph, 1))
# print(functions.extended_nearest_neighbour(graph))
# print(functions.OPT2(graph))
# print(functions.New_OPT2(graph))
