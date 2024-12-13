class Queue:     ## data structure
  def __init__(self,size):
    
    self.front = 0
    self.rear = -1
    self.maxSize = size
    self.queue = ["#" for x in range(self.maxSize)]   ## makes queue of specified size
    
  def seequeue(self):   ## prints queue
    print(self.queue)
    
    
  def isFull(self):    ## checks if full
    if self.rear+1 == self.maxSize:
      return True
    else:
      return False
      
  def isEmpty(self):    ## checks if empty
    if self.rear<self.front:
      return True
    else:
      return False
      
  def enqueue(self,data):     ## adds data to back of queue and increments self.rear
    if self.rear+1 == self.maxSize:
      print("queue is full")
    else:
      self.rear += 1
      self.queue[self.rear] = data
      
  def dequeue(self):   ## removes front value
    return self.queue[self.front] ## linear queue so just need to move front back instead of shift all forward
    self.front += 1
      
