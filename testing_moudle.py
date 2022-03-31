import os
import functions
import tsplib95
import functions
import networkx as nx
import glob
import json
import time

"""
def test from given path 
use it to open and solve tests
"""

collector = []
def test(path):
    print(path)
    global collector
    sizer = [200,5000,10000] 

    node_NN = 1
    file_number = 0
    for filename in os.listdir(path):
        file_number += 1
        if file_number > 20:
            break
        # print(filename)

        path_to_folder = path + "/" + filename
        path_to_tsp = r"" + path + "/" + filename + '/' + filename
        answer = set([os.path.dirname(p) for p in glob.glob(path_to_folder + "/*/*")])

        assert os.path.isfile(path_to_tsp)
        with open(path_to_tsp, "r") as f:

            print("Solving :" + filename)
            problem = tsplib95.read(f)
            graph = problem.get_graph()
            graph = graph.to_directed()

            if answer:
                path_to_tour = path_to_folder + "/" + filename.split('.')[0] + ".opt.tour" + "/" + filename.split('.')[0] + ".opt.tour"
                opt = tsplib95.load(path_to_tour)
                print("Rozwiązanie optymalne: ", problem.trace_tours(opt.tours))
            for i in sizer:
                start = time.process_time()
                permutation, solution = functions.k_random(graph, i)
                end = time.process_time()
    
                if not answer:
                    collector.append(DataGraph(filename, "KR-" + str(i), end - start, solution, str(permutation), "none"))
                else:
                    collector.append(DataGraph(filename, "KR-" + str(i), end - start, solution, str(permutation), opt.tours))
            print("KR")
            start = time.process_time()
            permutation, solution = functions.nearest_neighbour(graph, node_NN)
            end = time.process_time()
            print("NN")
            if not answer:
                collector.append(DataGraph(filename, "NN-" + str(node_NN), end - start, solution, str(permutation), "none"))
            else:
                collector.append(DataGraph(filename, "NN-" + str(node_NN), end - start, solution, str(permutation), opt.tours))

            start = time.process_time()
            permutation, solution = functions.extended_nearest_neighbour(graph)
            end = time.process_time()
            print("ENN")
            if not answer:
                collector.append(DataGraph(filename, "ENN", end - start, solution, str(permutation), "none"))
            else:
                collector.append(DataGraph(filename, "ENN", end - start, solution, str(permutation), opt.tours))

            start = time.process_time()
            permutation, solution = functions.opt2(graph)
            end = time.process_time()
            print(len(permutation))

            if not answer:
                collector.append(DataGraph(filename, "OPT2", end - start, solution, str(permutation), "none"))
            else:
                collector.append(DataGraph(filename, "OPT2", end - start, solution, str(permutation), opt.tours))
            
            start = time.process_time()
            permutation, solution = functions.opt2_2(graph)
            end = time.process_time()
            
            if not answer:
                collector.append(DataGraph(filename, "OPT2_2", end - start, solution, str(permutation), "none"))
            else:
                collector.append(DataGraph(filename, "OPT2_2", end - start, solution, str(permutation), opt.tours))
            
            start = time.process_time()
            permutation, solution = functions.opt2_3(graph)
            end = time.process_time()  
            print("2OPT2")
            if not answer:
                collector.append(DataGraph(filename, "OPT2_3", end - start, solution, str(permutation), "none"))
            else:
                collector.append(DataGraph(filename, "OPT2_3", end - start, solution, str(permutation), opt.tours))
                
    try:
        with open('C:/Users/denev/TSP/files7.json', 'w') as fout:
            json.dump(collector , fout)
    except IOError:
        pass
    finally:
        fout.close()


"""
dic to save data to JSON 
"""


def DataGraph(Filename, func, time, solution, permutation, opt ):
    Dic = {
        'file': Filename,
        'function': func,
        'time': time,
        'solution': solution,
        'optimal_solution': opt
        # 'memory'

    }
    return Dic


# def generate_graph(n, seed, type_of_problem):

"""
tests on auto generated graph
"""


def test_auto_generate(seed=100):
    types = ['sym', 'asym', 'full' 'eu']  # ADD undirected graph
    collection = []
    k = 200
    node_NN = 1
    sizer = [200,5000,10000] 
    
    for n in range(10, 40, 10):
        for graph_type in types:
            graph = functions.generate_graph(n, seed, graph_type)
            
            for i in sizer:
                start = time.process_time()
                permutation, solution = functions.k_random(graph, i)
                end = time.process_time()
                print("KR")
            
                collection.append(
                    DataGraph(graph_type + str(n), "KR-" + str(i), end - start, solution, str(permutation), "none"))

            start = time.process_time()
            permutation, solution = functions.nearest_neighbour(graph, node_NN)
            end = time.process_time()
            print("NN")

            collection.append(DataGraph(graph_type + str(n), "NN-" + str(node_NN), end - start, solution, str(permutation), "none"))

            start = time.process_time()
            permutation, solution = functions.extended_nearest_neighbour(graph)
            end = time.process_time()
            print("ENN")

            collection.append(DataGraph(graph_type + str(n), "ENN", end - start, solution, str(permutation), "none"))

            start = time.process_time()
            print("JFF")
            permutation, solution = functions.opt2(graph)
            end = time.process_time()

            start = time.process_time()
            permutation, solution = functions.opt2(graph)
            end = time.process_time()
           
            collector.append(DataGraph(graph_type + str(n), "OPT2", end - start, solution, str(permutation), "none"))
           
            start = time.process_time()
            permutation, solution = functions.opt2_2(graph)
            end = time.process_time()
            

            collector.append(DataGraph(graph_type + str(n), "OPT2_2", end - start, solution, str(permutation), "none"))

            
            start = time.process_time()
            permutation, solution = functions.opt2_3(graph)
            end = time.process_time()  
            print("2OPT2")
          
            collector.append(DataGraph(graph_type + str(n), "OPT2_3", end - start, solution, str(permutation), "none"))

    try:
        file = open("Test4", "w")
        json.dump(collection, file, indent=3)
    except IOError:
        pass
    finally:
        file.close()
