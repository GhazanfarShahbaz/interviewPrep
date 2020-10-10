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
