import math
import networkx as nx
import random 

def generate_corr_graph(corr):
    
    for first_el in corr:
        
        for second_el in corr:
            pass
            
            if first_el == second_el:
                continue
            #print(first_el,second_el)
           # print(first_el[0],second_el[0])         
            print(first_el[0],second_el[0],math.sqrt((float(first_el[1]) - float(second_el[1]))**2 + (float(first_el[2]) - float(second_el[2]))**2))
                    

def genrate_graph(n,min_number,max_number):
    
    new_graph = nx.complete_graph(n)
    
    for i in range(0,n):
        for j in range(0,n):
           new_graph[i][j]['weight'] = random.randrange(min_number,max_number)