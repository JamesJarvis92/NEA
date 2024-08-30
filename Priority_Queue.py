class Builder:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority
        
class PQueue:
    def __init__(self):
        self.queue = list()
        
    def insert(self,node):
        inserted = False    ## stops adding same thing twice
        if self.size() == 0:
            if inserted == False:
                self.queue.append(node)
                inserted = True
        else:
            for i in range(0,self.size()):
                if node.priority >= self.queue[i].priority:
                    if i == (self.size()-1):
                        if inserted == False:
                            self.queue.insert(i+1, node)
                            inserted = True
                    else:
                        pass
                else:
                    if inserted == False:
                        self.queue.insert(i, node)
                        inserted = True
    

    def getlist(self):
        l = []
        for i in self.queue:
            l.append([i.data,i.priority])
        return l
    

    def delete(self):
        return self.queue.pop(0)
    
    def size(self):
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