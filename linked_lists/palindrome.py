from linkedList import LinkedList
from linkedList import Node
from linkedList import list_to_linkedList


def palindrome(l: Node, curr = 0, size = [0], strs = ["",""]) -> bool:
    if(l):
        size[0] = curr
        palindrome(l.next, curr+1, size, strs)

        if(size[0]%2 == 1 and curr >= size[0]-1):
            strs[1] += l.val
        elif(curr > int(size[0]/2) and size[0]%2 == 0):
            strs[1] += l.val
        elif(curr < int(size[0]/2)):
            strs[0] = f"{strs[0]}{l.val}"

    if(curr == 0):
        print(strs)
        return strs[0] == strs[1]

if __name__ == "__main__":
    print(palindrome(list_to_linkedList(['a','a','b','a','a']).head))
