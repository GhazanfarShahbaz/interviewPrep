from stack import stack
from random import randrange

class sortStack:
    def __init__(self):
        self.sorted = stack()
        self.toSort = stack()

    def push(self,val):
        while(not self.sorted.isEmpty() and self.sorted.peek() > val):  # Moves elements to other stack until the next value ins tackk is less than value
            self.toSort.push(self.sorted.pop())
        
        self.sorted.push(val)

        while(not self.toSort.isEmpty()):
            self.sorted.push(self.toSort.pop())

    def peek(self):
        return self.sorted.peek()

    def pop(self):
        return self.sorted.pop()

    def print(self):
        print(self.sorted)

if __name__ == "__main__":
    sort = sortStack()
    for x in range(1000):
        sort.push(randrange(-100,100))
    sort.print()