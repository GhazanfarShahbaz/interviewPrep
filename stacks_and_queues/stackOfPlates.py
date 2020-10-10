
class stackOfPlates:
    def __init__(self):
        self.plates = []
        self.current = -1
        self.threshold = 100

    def push(self, value):
        if self.current == -1 or len(self.plates[self.current]) == self.threshold:
            self.current += 1
            self.plates.append([value])
        else:
            self.plates[self.current].append(value)
    
    def pop(self):
        if len(self.plates)-1 != self.current or len(self.plates[self.current]) == 0:
            self.plates.pop()
            self.current -= 1
        if self.current != -1:
            value = self.plates[self.current].pop()
            # if len(self.plates[self.current]) == 0:
            #     self.plates.pop()
            return value
        
    def peek(self):
        if len(self.plates)-1 != self.current or len(self.plates[self.current]) == 0:
            self.plates.pop()
            self.current -= 1
        if self.current != -1:
            self.plates[self.current][-1]

    def isEmpty(self):
        return len(plates) != 0 and len(plates[0]) != 0

    def popAt(self, index):
        if (len(self.plates) > index and len(self.plates[index]) > 0):
            value = self.plates[index].pop()
            if(not self.plates[index]):
                self.plates.pop(index)
                self.current -= 1
            return value
            

    def __str__(self):
        string = ""
        for x in self.plates:
            string += f"{len(x)} \n"
        #     for y in x:
        #         string += f"{y} "
        # string += "\n\n"
        return string
            
if __name__ == "__main__":
    stack = stackOfPlates()
    for x in range(1000):
        stack.push(x)
        
    print(stack)

    for x in range(100):
        stack.popAt(1)

    print(stack)