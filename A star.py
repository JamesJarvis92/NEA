from Priority_Queue import *

def h(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    
    return abs(x1-x2) + abs(y1-y2)
