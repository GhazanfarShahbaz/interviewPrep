from stack import stack


class queueWithStacks:
    def __init__(self):
        self.old = stack()
        self.new = stack()
        self.parse = False

    def transfer(self):
        if self.old.isEmpty():
            while(not self.new.isEmpty()):
                self.old.push(self.new.pop())   # Transfers if empty, all such that the elements are reversed

    def push(self,value):
        self.new.push(value)

    def peek(self):
        self.transfer()
        return self.old.peek()

    def pop(self):
        self.transfer()
        return self.old.pop()


    
if __name__ == "__main__":
    queue = queueWithStacks()

    for x in range(10):
        queue.push(x)
    
    for y in range(7):
        print(queue.pop())

    for x in range(10):
        queue.push(x)

    for y in range(7):
        print(queue.pop())

    