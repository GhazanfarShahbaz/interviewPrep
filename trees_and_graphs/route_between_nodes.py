from graph import Graph
from graph import Node
from collections import s

class stack:
    def __init__(self):
        self.values = []

    def isEmpty(self):
        return len(self.values) == 0

    def pop(self):
        if not self.isEmpty():
            return self.values.pop()

    def push(self, val):
        self.values.append(val)

    def peek(self):
        if not self.isEmpty():
            return self.values[len(self.values) -1]

    def __str__(self):
        string =""
        for x in self.values:
            string += f"{x} "
        return string

def allChildrenChecked(current):
    for x in current:
        if not x.visited:
            return False
    return True


def pathBetweenNodes(pathOne: Node, pathTwoNode: Node) -> bool:
    current = pathOne
    position = Stack()
    position.push(current)

    while(not position.isEmpty()):
        for x in position.peek().children:
            if x == pathTwoNode:
                return True
            elif not x.visited:
                current.visited = True
                position.push(current)
                break
        if allChildrenChecked(position.peek()):
            position.pop()

    return False

