class Queue:
    # here we have defined a queue data structure with its operations
    def __init__(self):
        self.queue = []
        #this is the class attribute which is initialized to an empty list
        #but we can not directly perform operations on this list
        # we have to perform operations only thorugh the class methods, so that it will behave as a queue.

    def addq(self, v):
        self.queue.append(v)
        # in the queue, element will always be added in the end of the queue
        # this method will take a given element(vertex v) as input and add it to the last position in the list.
    
    def delq(self):
        # in the queue , element will always be deleted from the beginning of the queue.
        v = None # first, we initialize a variable with None which will store the deleted element
        if not self.isempty(): 
            v = self.queue[0] # if the queue is not empty then, we first copy the first element to the v variable
            self.queue = self.queue[1:] # and then, using the list trim operation we delete the first element.
        return v

    def isempty(self):
        # this method will retun true if the queue is empty, otherwise it will return false.
        return (self.queue == [])
    
    def __str__(self):
        return str(self.queue)

