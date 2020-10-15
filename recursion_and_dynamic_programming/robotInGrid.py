class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def peek(self):
        return self.stack[-1]
    def pop(self):
        return self.pop()
    def isEmpty(self):
        return len(self.stack) == 0

    def stackToList(self):
        string = ""
        for x in range(1,self.stack):
            if self.stack[x]

def robotInGrid(grid: list, int row, int col) -> list:
    if not grid:
        return [None]

    visited = [[None]*len(col)] * len(row)
    path = Stack()
    visited[0][0] = True
    path.append(grid[0][0])
    currentCol = 0
    currRow = 0
    while(path):
        if currCol+1 <= Col and grid[currCol+1][currentCol] and not visited[currCol+1][currentCol]:
            currentCol += 1
            visited[currentCol][currRow] = True
            path.append("Down")
        elif currRow+1 <= row and grid[currentCol][currRow]  and not visited[currentCol][currRow+1]:
            currRow += 1
            visited[currentCol][currRow] = True
            path.append("Right")
        else:
            direction = path.pop()
            if direction = "Right":
                currRow -= 1
            else:
                currCol -= 1

    return path.stackToList()
