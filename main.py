import tsplib95
import functions


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
    
    opt = tsplib95.load('bayg29.opt.tour')
    print(opt)
    print(problem.trace_tours(opt.tours))
    return new_graph


if __name__ == '__main__':
    graph = read_graph('bayg29.tsp')

    print(functions.k_random(graph, 2000))
    print(functions.nearest_neighbour(graph, 1))
    print(functions.extended_nearest_neighbour(graph))
    functions.OPT2(graph)
