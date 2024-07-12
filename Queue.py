class Queue:
  def __init__(self):
    
    self.front = 0
    self.rear = -1
    self.maxSize = 999
    self.queue = ["#" for x in range(self.maxSize)]
    
  def seequeue(self):
    print(self.queue)
    
    
  def isFull(self):
    if self.rear+1 == self.maxSize:
      return True
    else:
      return False
      
  def isEmpty(self):
    if self.rear<self.front:
      return True
    else:
      return False
      
  def enqueue(self,data):
    if self.rear+1 == self.maxSize:
      print("queue is full")
    else:
      self.rear += 1
      self.queue[self.rear] = data
      
  def dequeue(self):
    if isEmpty():
      print("list is empty")
    else:
      return self.queue[self.front] ## linear queue so just need to move front back instead of shift all forward
      self.front += 1
      
myqueue = Queue()
myqueue.enqueue("hello1")
myqueue.enqueue("hello2")
myqueue.enqueue("hello3")
myqueue.dequeue()
myqueue.seequeue()