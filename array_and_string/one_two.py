"""Challenge 1.2
Question: Given 2 strings, write a method to decide of one is a
permutation of the other """

testList = [
    ['abc', 'bac'],
    ['a', 'b'],
    ['', 'v'],
    ['aaaaaaaaaa', 'aaaaaaaava']
    ]


def checkPermutation(strOne, strTwo):
    if(len(strOne) != len(strTwo)):
        return False

    listOne = list(strOne)
    for x in strTwo:
        try:
            listOne.remove(x)
        except:
            return False
        else:
            continue
    print(listOne)
    return True


if __name__ == "__main__":
    for x in testList:
        print(x[0], x[1], checkPermutation(x[0], x[1]))
    
