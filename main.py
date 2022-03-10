import networkx as nx
import matplotlib.pyplot as plt

Graph = nx.DiGraph()


with open("bays29.tsp", 'r', encoding = 'utf-8') as file:
   
    # reading each line    
    for line in file:
        
        if ("DIMENSION" in line):
           nb_cities = line.split(': ')[1]  
           print(nb_cities)
           
        elif ("EDGE_WEIGHT_SECTION" in line):
            break
     
    city = 0
    connection_to_city =  0
    for line in file:
        connection_to_city =  0
        for sign in line.split(' '):
                  
            if ("DISPLAY_DATA_SECTION" in line):
                break
            
            try :
                if city != connection_to_city:
                    Graph.add_edge(city, connection_to_city, weight= int(sign)) 
            
            except ValueError:
               pass
           
            connection_to_city = connection_to_city + 1
        
        city = city + 1    
        if ("DISPLAY_DATA_SECTION" in line):
            break

def generator():
    
    pass
    