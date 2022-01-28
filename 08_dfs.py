
import numpy as np
A = np.zeros(shape=(10,10))
edges = [(0,1), (0,4), (1,2), (2,0), (3,4), (3,6), (4,0), (4,3), (4,7), (5,3), (5,7), (6,5),(7,4), (7,8), (8,5), (8,9), (9,8)]
for (i,j) in edges:
    A[i,j] = 1

def neighbours(Amat, x):
    (rows, cols) = Amat.shape
    nbrs = []
    for j in range(cols):
        A[x,j] = nbrs.append(j)
    return nbrs

def dfsinit(Amat):
    (rows,cols) = Amat.shape
    (visited, parents) = ({},{})
    for i in range(rows):
        visited[i] = False
        parents[i] = -1
    return (visited, parents)

def dfs(Amat, visited, parents, v):
    visited[v] = True

    for k in neighbours(Amat, v):
        if(not visited[k]):
            parents[k] = v
            (visited, parents) = dfs(Amat, visited, parents, k)

    return (visited, parents)


