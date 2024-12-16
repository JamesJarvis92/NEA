class Builder:    ##  nodes for priority queue
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority
        
class PQueue:     ## data structure
    def __init__(self):
        self.queue = list()
        
    def insert(self,node):
        inserted = False    ## stops adding same thing twice
        if self.size() == 0:
            if inserted == False:
                self.queue.append(node)
                inserted = True
        else:
            for i in range(0,self.size()):     ## loops until it finds valid position for new node
                if node.priority >= self.queue[i].priority:
                    if i == (self.size()-1):
                        if inserted == False:
                            self.queue.insert(i+1, node)    ## inserts and changes insert to true
                            inserted = True
                    else:
                        pass
                else:
                    if inserted == False:   ## adds to end of queue
                        self.queue.insert(i, node)
                        inserted = True
    

    def getlist(self):    ## returns list of data and their priorities
        l = []
        for i in self.queue:
            l.append([i.data,i.priority])
        return l
    
    def frontval(self):      ## gets front value
        return self.queue[0]
    
    def delete(self):      ## returns data at front and removes 
        data = self.queue.pop(0)
        return data.data
    
    def size(self):    ## size of queue
        return len(self.queue)
"""    
b1 = Builder("C",3)
b2 = Builder("D",7)
b3 = Builder("B",12)
b4 = Builder("A",15)
pq = PQueue()
print(pq.getlist())
pq.insert(b1)
pq.insert(b2)
pq.insert(b3)
pq.insert(b4)
print(pq.getlist())
"""