"""Challenge 1.1
Question: Implement an algorithm to determine if a string ha all uniuqe
characters. What if you could not use additional characters"""

import random


def testList():
    """Genrates 255 random test strings"""
    testList = []
    for x in range(50):
        newString = ""
        for y in range(random.randint(0,50)):
            # if(random.randint(0,1) == 1):
            newString += chr(random.randint(97, 122))
            # else:
            #     newString += chr(random.randint(65, 90))
        testList.append(newString)
    return testList


def isUnique(case):
    """Super fast"""
    return len(case) == len(''.join(set(case))) #Set removes any duplicate elements, join converts to one string


def withoutExtraStructures(case):
    """O(n^2) time complexity"""
    for x in range(len(case)):
        for y in range(x+1, len(case)):
            if case[x] == case[y]:
                return False
    return True


if __name__ == "__main__":
    for x in testList():
        print(x)
        if isUnique(x) != withoutExtraStructures(x):
            print("TEST Failed", x, isUnique(x), withoutExtraStructures(x))