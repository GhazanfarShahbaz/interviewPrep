class stack:
    def __init__(self):
        self.values = []

    def isEmpty(self):
        return self.values.length == 0

    def pop(self):
        if not self.isEmpty():
            return self.values.pop()

    def push(self, val):
        self.values.append():

    def peek(self):
        if not self.isEmpty():
            return self.values[values.length -1]
