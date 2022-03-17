import networkx as nx
import matplotlib.pyplot as plt
import functions


Graph = nx.DiGraph()


with open("berlin52.tsp", 'r', encoding = 'utf-8') as file:
   
    # reading each line    
    for line in file:
        
        if ("DIMENSION" in line):
           nb_cities = line.split(': ')[1]  
           print(nb_cities)
           
        # Settings to read type of Matrix 
        if("EDGE_WEIGHT_FORMAT" in line):
            if ("FULL_MATRIX " in line ): 
                set_flag_type = 0
            elif ("UPPER_ROW" in line ): 
                set_flag_type = 1
                
        elif("EUC_2D" in line):  
            set_flag_type = 2
            
        elif ("EDGE_WEIGHT_SECTION" in line) or ("NODE_COORD_SECTION" in line):
            break
     
    city = 0
    connection_to_city =  0
    iterator = 0 
    coordinates = []
    for line in file:
            
        connection_to_city =  0
            
        if set_flag_type == 1:
            connection_to_city = iterator + 1  
                
        for valuve in line.split():
             
            if ("DISPLAY_DATA_SECTION" in line):
                       break
                   
            if set_flag_type == 0 :
                        
                if city != connection_to_city:
                    print(city,connection_to_city , int(valuve))
                    Graph.add_edge(city, connection_to_city, weight= int(valuve)) 
                        
                     
                       
            elif set_flag_type == 1:
                        
                print(city,connection_to_city , int(valuve))
                Graph.add_edge(city, connection_to_city , weight= int(valuve)) 
                Graph.add_edge(connection_to_city, city, weight= int(valuve)) 
                        
            connection_to_city = connection_to_city + 1
            
            
        if set_flag_type== 2  and "EOF" not in line:
            
            # print(line)
             coordinates.append(line.strip().split())
             
        city = city + 1 
        iterator = iterator + 1
        if ("DISPLAY_DATA_SECTION" in line):
            break
   
             
            #print(first_cor[0],second_cor[0],math.sqrt((float(first_cor[1]) - float(second_cor[1]))**2 + (float(first_cor[2]) - float(second_cor[2]))**2))
    if set_flag_type == 2:
        functions.generate_corr_graph(coordinates)
        
    print(list(Graph.nodes()))

    
    

# Graf pełny vs graf skierowany?

