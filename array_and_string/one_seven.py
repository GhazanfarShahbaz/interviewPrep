""" Challenge 1.8: Rotate Matrix
Given an image represented by a N*N matrix, where each pxel in the image is 4 bytes, write a method to rotate the imageby 90 degrees. Can you do this in place?"""

test = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

testTwo = [
    [1,1,1,1,1],
    [2,2,2,2,2],
    [3,3,3,3,3],
    [4,4,4,4,4],
    [5,5,5,5,5,]
]

def rotate_matrix(arr: list):
    if(not arr):
        return
    size = len(arr)
    for x in range(size//2):
        first = x
        last = size -1 - x
        for parse in range(first, last):
            offset = parse - first
            top = arr[first][parse]

            arr[first][parse] = arr[last-offset][first]
            arr[last-offset][first] = arr[last][last-offset]
            arr[last][last-offset] = arr[parse][last]
            arr[parse][last]= top

    return arr 


if __name__ == "__main__":
    for x in rotate_matrix(testTwo):
        print(x)
