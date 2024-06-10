class Stack:
  def __init__(self, size):
    self.size = size
    self.stack = []
    self.top = -1
    for i in range(size):
      self.stack.append("#")
      
  def push(self, item):
    if self.top == self.size:
      return "Stack is full"
    else:
      self.top += 1
      self.stack[self.top] = item
    
  def spop(self):
    if self.top >= 0:
      item = self.stack[self.top]
      self.stack[self.top] = "#"
      self.top -= 1
      return item
    else:
      return "Can't pop stack is empty"
      
  def isFull(self):
    if self.top == self.size-1:
      return True
    else:
      return False
  
  def isEmpty(self):
    if self.top == -1:
      return True
    else:
      return False
      
  def seestack(self):
    return self.stack
  
  def peek(self):
    return self.stack[self.top]
