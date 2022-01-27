import numpy as np

A = np.zeros(shape = (10,10))
edges = [(0,1), (0,4), (1,2), (2,0), (3,4), (3,6), (4,0), (4,3), (4,7), (5,3), (5,7), (6,5),(7,4), (7,8), (8,5), (8,9), (9,8)]
for (i,j) in edges:
    A[i,j] = 1

class Queue:
    def __init__(self):
        self.queue = []

    def addq(self, v):
        self.queue.append(v)
    
    def delq(self):
        v = None
        if not self.isEmpty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return v
    
    def isEmpty(self):
        return (self.queue==[])


def neighbours(Amat,v):
    (rows,cols) = Amat.shape
    nbrs = []
    for j in range(cols):
        if Amat[v,j] == 1:
            nbrs.append(j)
    return nbrs
    
def bfs(Amat,x):
    (rows,cols) = Amat.shape
    visited = {}

    for i in range(rows):
        visited[i] = False
    
    q = Queue()

    visited[x] = True
    q.addq(x)

    while(not q.isEmpty()):
        j = q.delq()
        for k in neighbours(Amat,j):
            if (not visited[k]):
                visited[k] = True
                q.addq(k)
        
    return (visited)

print(bfs(A, 2))





    