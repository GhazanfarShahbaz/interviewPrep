import random
import time
class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, value):
        self.stack.append(value)
        if len(self.minimum) == 0:
            self.minimum.append(value)
        else:
            if self.minimum[0] >= value:
                self.minimum.insert(0, value)
            elif self.minimum[-1] < value:
                self.minimum.append(value)
            else:
                parse = len(self.minimum)//2
                count = 0
                while(True):
                    if(self.minimum[parse] > value):
                        # print(parse, self.minimum[parse], value)
                        parse = parse//2
                    elif self.minimum[parse] < value:
                        parse = parse + parse//2
                    if parse-1 >=0 and self.minimum[parse-1] < value and self.minimum[parse] > value:
                        self.minimum.insert(parse, value)
                    count +=1
                    if count == 100:
                        print(parse, self.minimum[parse], value)
                        break
                    # try:
                    #     if(self.minimum[parse] > value):
                    #         parse = parse//2
                    #     elif(self.minimum[upper] < value):
                    #         upper = upper + (parse)//2
                    #     else:
                    #         self.minimum.insert(upper, value)
                    #         break
                    # except:
                    #     print(upper, len(self.minimum)-1)
                    #     break

                    # if self.minimum[upper] < value:
                    #     upper = (upper+parse)//2
                    # elif self.minimum[parse] > value:
                    #     parse = (upper*parse)//2
                    
                    # if self.minimum[upper] <= value and self.minimum[parse] >= value:
                    #     self.minimum.insert(upper,value)
                    # if self.minimum[upper] == value:
                    #     self.minimum.insert[upper,value]
                    # elif self.minimum[parse] == value:
                    #     self.minimum.insert(parse,value)
                    
                    # if self.minimum[parse] < value and len(self.minimum) < parse+1 and self.minimum[parse+1] < value:
                    #     parse = parse*(parse//2)
                    # elif self.minimum[parse] > value and len(self.minimum) < parse+1 and self.minimum[parse+1] > value:
                    #     parse = parse//2
                    # else:
                    #     self.minimum.insert(parse,value)
                    #     break
    
    def pop(self):
        value = self.stack.pop()
        self.minimum.remove(value)
        return value
    
    def peek(self):
        return self.stack[len(self.stack)-1]
    def min(self):
        if self.minimum:
            return self.minimum[0]
        else:
            return None

    def __str__(self):
        vals = ""
        for x in self.minimum:
            vals += f"{x} "
        return vals

        
if __name__ == "__main__":
    values = MinStack()
    test = []
    start = time.time()
    for x in range(10000):
        test.append(random.randrange(-100000000,1000000000))
        values.push(test[-1])
    print(time.time() - start)
    # start = time.time()
    # print(values.min())
    # # print(time.time() - start)
    # start = time.time()
    # print(min(test))
    # # print(time.time() - start)


    # print(values)


