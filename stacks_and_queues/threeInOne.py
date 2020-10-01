"""3.1: Three in One
Describe how you would ise a single array to implement three stacks"""


class threeInOne:
    def __init__(self):
        self.arr = []
        self.first = 0
        self.second = 0
        self.third = 0

    def resize(stackNum, amount, action: str, val = None):
        if stackNum == 1 and (((action == "pop" or action == "peek") and self.first > 0) or action == "push" or action == "size"):
            if action == "pop":
                self.first -= 1
                return self.arr.pop(self.first - 1)
            elif action == "peek":
                return self.arr[self.first - 1]
            elif action == "push":
                self = self[:first] + [val] + self[first:]
                self.first += 1
            elif action == "size":
                return self.first
        if stackNum == 2 and (((action == "pop" or action == "peek") and self.third > 0) or action == "push" or action == "size"):
            if action == "pop":
                self.second -= 1
                return self.arr.pop(self.second - 1)
            elif action == "peek":
                return self.arr[self.second - 1]
            elif action == "push":
                self.arr[:] = self[:second] + [val] + self[second:]
                self.second += 1
            elif action == "size":
                return self.first
        elif stackNum == 3 and (((action == "pop" or action == "peek") and self.third > 0) or action == "push" or action == "size"):
            if action == "pop":
                self.third -= 1
                return self.arr.pop()
            elif action == "peek":
                return self.arr[self.arr.length - 1]
            elif action == "push":
                self.arr.append(val)
                self.third += 1
            elif action == "size":
                return self.first
  
    def push(self, stackNum, val):
        if stackNum > 0 and stackNum <= 3:
            self.resize(stackNum, 1, "push", val)

    def peek(self, stackNum, val):
        if stackNum > 0 and stackNum <= 3:
            return self.resize(stackNum, 0, "peek")

    def pop(self, stackNum, val):
        if stackNum > 0 and stackNum <= 3:
            return self.resize(stackNum, -1, "pop")
        
    def stackSize(self, stackNum):
         if stackNum > 0 and stackNum <= 3:
            return self.resize(stackNum, 0, "size")
            
        