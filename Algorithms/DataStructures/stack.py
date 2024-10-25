class Stack:
  def __init__(self, size):
    self.size = size
    self.stack = []
    self.top = -1
    for i in range(size): ## makes stack large array of #'s
      self.stack.append("#")
      
  def push(self, item):  ## adds to stack
    if self.top == self.size:
      return "Stack is full"
    else:
      self.top += 1
      self.stack[self.top] = item
    
  def spop(self):   ## can't call pop because python already has a .pop()
    if self.top >= 0:
      item = self.stack[self.top]
      self.stack[self.top] = "#"
      self.top -= 1
      return item
    else:
      return "Can't pop stack is empty"
      
  def isFull(self):   ## checks if full
    if self.top == self.size-1:
      return True
    else:
      return False
  
  def isEmpty(self):    ## checks if empty
    if self.top == -1:
      return True
    else:
      return False
      
  def seestack(self):   ## returns stack
    return self.stack
  
  def peek(self):    ## look at top element of stack
    return self.stack[self.top]
  
  
