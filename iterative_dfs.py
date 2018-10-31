from collections import deque
from time import sleep
import keyboard
import queue

class Node :
    def __init__(self,in_x=0,in_y=0):
         self.x = in_x
         self.y = in_y
         self.data = None
         self.visited = False
         self.added = False

    def __str__(self):
        #return str((self.x,self.y,self.data))
        return str(self.data)
