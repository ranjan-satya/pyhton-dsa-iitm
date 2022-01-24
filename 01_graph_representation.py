'''A graph can be represented in two ways:
  1. adjecency matrix
  2. adjecency list 
'''
# 1.
    # For representing in adjecency matrix form we will use the numpy array
    # to use the numpy, first we have to import it
import numpy as np
    # if it is not installed , the we have install it using pip install command

A = np.zeros(shape = (10,10))
    # this will create a 10*10 matrix with 0 as the value at each index

edges = [(0,1), (0,4), (1,2), (2,0), (3,4), (3,6), (4,0), (4,3), (4,7), (5,3), (5,7), (6,5),(7,4), (7,8), (8,5), (8,9), (9,8)]
    # this is the given input graph where each tuple represents an edge in the graph.

for (i,j) in edges:
    A[i,j] = 1 # A[i,j] represents the position at ith row and jth column.
    # this loop will change the values to 1 at those indexes where the index value mathces with the edge
    # rest other values will remain as it is.

print(A)
    # to check whether the matrix is created correctly or not , we have printed the matrix
 

#2. 
    # For representing in adjecency list from we will use python dictionary data structure.

Alist = {} # creates an empty dictionary
for i in range(10):            
    Alist[i] = []        # will create a dictionary with 0,1,....9 as keys and [] as value for each of the keys.

for (i,j) in edges:             
    Alist[i].append(j)  # will add the neighbouring vertices of each vertex to the corresponding keys.

print(Alist)

        