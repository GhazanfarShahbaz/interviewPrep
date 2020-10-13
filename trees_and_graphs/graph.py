class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.visited = False
    def addPath(self,value):
        self.children.append(value)

class Graph:
    def __init__(self):
        self.paths = []



    
        