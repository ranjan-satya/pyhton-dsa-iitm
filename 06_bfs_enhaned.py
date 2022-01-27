import numpy as np

A = np.zeros(shape = (10,10))
edges = [(0,1), (0,4), (1,2), (2,0), (3,4), (3,6), (4,0), (4,3), (4,7), (5,3), (5,7), (6,5),(7,4), (7,8), (8,5), (8,9), (9,8)]
for (i,j) in edges:
    A[i,j] = 1

def neighbours(Amat, x):
    nbrs = []
    (rows, cols) = Amat.shape
    for j in range(cols):
        if Amat[x,j] == 1:
            nbrs.append(j)
    return nbrs

class Queue:
    def __init__(self):
        self.queue = []
    
    def addq(self, x):
        self.queue.append(x)
    
    def delq(self):
        v = None
        if not self.isEmpty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
    def isEmpty(self):
        return (self.queue == [])
    
def bfs(Amat, x):
    (rows,cols) = Amat.shape
    (visited,parents) = ({},{})

    for i in range(rows):
        visited[i] = False
        parents[i] = -1
    
    q = Queue()

    visited[x] = True
    q.addq(x)

    while (not q.isEmpty()):
        j = q.delq()
        for k in neighbours(Amat,j):
            if not visited[k]:
                visited[k] = True
                parents[k] = j
                q.addq(k)

    return (visited,parents)

print(bfs(A, 2))
