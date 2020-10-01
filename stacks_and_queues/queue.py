class queue:
    def __init__(self):
        values = []

    def isEmpty(self):
        return self.values.length == 0

    def push(self, val):
        self.values.append(val)

    def remove(self):
        if not self.isEmpty():
            return self.values.pop(0)

    def peek(self):
        if not self.isEmpty():
            return self.values[0]
