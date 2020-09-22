"""Challenge 1.8: Zero Matrix
Write an algorithm such that is an element in an MxN matrix is 0, its entire row and column are set to 0 """

test = [
    [0,1,1],
    [1,2,3],
    [1,0,1],
]


def zero_matrix(matrix: list) -> None:
    columns = []
    row = []

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:
                if x not in columns:
                    columns.append(x)
                if y not in columns:
                    row.append(y)
    
    for x in columns:
        for a in range(len(matrix[x])):
            matrix[x][a] = 0
    for y in row:
        for a in range(len(matrix)):
            matrix[a][y] = 0

    for l in matrix:
        print(l)

if __name__ == "__main__":
    for l in test:
        print(l)
    print(" ")
    zero_matrix(test)