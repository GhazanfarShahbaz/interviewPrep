import copy
def powerSet(arr: list)-> set:
    values = []
    
    for x in range(len(arr)):
        values.append(0)
    powerSetIndexes = [[values]]

    for y in range(0, len(arr)):
        values[y] = 1
        permute(values , 0 , len(values)-1, powerSetIndexes)  

    powerSet = []

    for x in range(0, len(powerSetIndexes)):
        current = []
        for z in range(len(powerSetIndexes[x])):
            if powerSetIndexes[x][z] == 1:
                current.append(arr[z])
        powerSet.append(current)

    return sorted(set(map(tuple, powerSet)), key=len)

def permute(a: list, leftBound: int, rightBound: int, permutations: list):
    if leftBound == rightBound and a not in permutations: 
        permutations.append(copy.copy(a))                             # appends to the permutation list
    else: 
        for i in range(leftBound, rightBound+1):
            a[leftBound], a[i] = a[i], a[leftBound]             # shifts the character
            permute(a, leftBound+1, rightBound, permutations)   # uses a recursion to shift the next characters
            a[leftBound], a[i] = a[i], a[leftBound]             # changes to original


if __name__ == "__main__":
    print(powerSet([1,2,3,4,5,6,7,8]))