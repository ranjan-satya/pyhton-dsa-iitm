edges = [(0,1), (0,4), (1,2), (2,0), (3,4), (3,6), (4,0), (4,3), (4,7), (5,3), (5,7), (6,5),(7,4), (7,8), (8,5), (8,9), (9,8)]

Alist = {} # creates an empty dictionary
for i in range(10):            
    Alist[i] = []        

for (i,j) in edges:             
    Alist[i].append(j)

def neighbours(Alist, i):
    return Alist[i]             # since, the value of the key contains the neighbouring vertices, we can directly return them.

print(neighbours(Alist, 5))