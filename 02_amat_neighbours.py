edges = [(0,1), (0,4), (1,2), (2,0), (3,4), (3,6), (4,0), (4,3), (4,7), (5,3), (5,7), (6,5),(7,4), (7,8), (8,5), (8,9), (9,8)]
    # this is the given input graph where each tuple represents an edge in the graph.

import numpy as np
A = np.zeros(shape = (10,10))

for (i,j) in edges:
    A[i,j] = 1

def neighbours(Amat,i):
    # this will take a graph A as input which is there in the form of adjecency matrix and a node i.
    # and will give the neighbouring nodes of the given node i 
    nbrs = []
    (rows, cols) = Amat.shape # shape method in the numpy array will return the shape of the matrix as a tuple

    for j in range(cols):
        # traverse through each of the columns of the matrix
        if Amat[i,j] == 1: # the value is 1 at the Index (i,j), means there is an edge between the i  node and the j node
            nbrs.append(j)
    
    return nbrs

print(neighbours(A, 5))