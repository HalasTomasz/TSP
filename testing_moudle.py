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
def test(path):
    print(path)
    collector =[]
    k = 200
    node_NN = 1
    for filename in os.listdir(path):
        #print(filename)
        
        path_to_folder = path+"/"+filename 
        path_to_tsp = r"" + path +"/"+filename+'/'+filename
        answer = set([os.path.dirname(p) for p in glob.glob(path_to_folder+"/*/*")])
        

        assert os.path.isfile(path_to_tsp)
        with open(path_to_tsp, "r") as f:
            
             
             print("Solving :" + filename)
             problem = tsplib95.read(f)
             graph = problem.get_graph()
             graph = graph.to_directed()
             
             if answer:
                 path_to_tour = path_to_folder +"/"+filename.split('.')[0]+".opt.tour"+"/" +filename.split('.')[0]+".opt.tour"
                 opt = tsplib95.load(path_to_tour)
                 print("Rozwiązanie optymalne: ", problem.trace_tours(opt.tours))
                 

             start = time.time()
             permuation,solution  = functions.k_random(graph, k)
             end = time.time()
             print("KR")
             
             if not answer:
                 collector.append(DataGraph(filename,"KR-" + str(k), end - start, solution,str(permuation),"none"))                      
             else:
                 collector.append(DataGraph(filename,"KR-" + str(k), end - start, solution,str(permuation),opt))
             
             start = time.time()
             permuation,solution  = functions.nearest_neighbour(graph, node_NN)
             end = time.time()
             print("NN")
             if not answer:
                 collector.append(DataGraph(filename,"NN-" + str(node_NN), end - start, solution, str(permuation), "none"))                      
             else:
                 collector.append(DataGraph(filename,"NN-" + str(node_NN), end - start, solution, str(permuation), opt))
                 
             
             start = time.time()
             permuation,solution  = functions.extended_nearest_neighbour(graph)
             end = time.time()
             print("ENN")
             if not answer:
                 collector.append(DataGraph(filename,"ENN", end - start, solution,str(permuation),"none"))                      
             else:
                 collector.append(DataGraph(filename,"ENN", end - start,solution,str(permuation),opt))
             
             start = time.time()
             permuation,solution  = functions.New_OPT2(graph)
             end = time.time()
             print("2OPT")
             
             if not answer:
                 collector.append(DataGraph(filename,"OPT2", end - start, solution,str(permuation),"none"))                      
             else:
                 collector.append(DataGraph(filename,"OPT2", end - start,solution,str(permuation),opt))
             break
    try:
        file = open("File", "w")
        json.dump(collector,file, indent=3)
    except IOError:
        pass
    finally:
        file.close()  

"""
dic to save data to JSON 
"""
def DataGraph(Filename,func,time,solution, permutation, opt, ):
    
    Dic={
        'file':Filename,
        'function':func,
        'time':time,
        'soultion':solution,
        'permutation':permutation,
        'optimal_soultion': opt
        #'memory'
        
        }
    return Dic
    
#def generate_graph(n, seed, type_of_problem):

"""
tests on auto generated graph
"""
def test_auto_generate(seed = 100):
    types = ['sym', 'asym','full' 'eu']  #ADD undiritected graph
    collection = []
    k = 200
    node_NN = 1
    for n in range(100,200,100): 
        for graph_type in types:
            
            graph = functions.generate_graph(n, seed, graph_type)
            
            start = time.time()
            permuation,solution  = functions.k_random(graph, k)
            end = time.time()
            print("KR")
            
            collection.append(DataGraph(graph_type + str(n),"KR-" + str(k), end - start, solution,str(permuation),"none"))                      
            
            
            start = time.time()
            permuation,solution  = functions.nearest_neighbour(graph, node_NN)
            end = time.time()
            print("NN")
           
            collection.append(DataGraph(graph_type + str(n),"NN-" + str(node_NN), end - start, solution, str(permuation), "none"))                      
          
            start = time.time()
            permuation,solution  = functions.extended_nearest_neighbour(graph)
            end = time.time()
            print("ENN")
            
            collection.append(DataGraph(graph_type + str(n),"ENN", end - start, solution,str(permuation),"none"))                      
        
            start = time.time()
            permuation,solution  = functions.OPT2(graph)
            end = time.time()
            print("2OPT")
          
            collection.append(DataGraph(graph_type + str(n),"OPT2", end - start, solution,str(permuation),"none"))                      
          
        
            
    try:
        file = open("Test", "w")
        json.dump(collection,file, indent=3)
    except IOError:
        pass
    finally:
        file.close()  

           
