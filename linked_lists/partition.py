from linkedList import LinkedList
from linkedList import Node
from linkedList import list_to_linkedList


def partition(chain: Node, target: int) -> LinkedList:
    beforeStart = Node()
    beforeEnd = Node()
    afterStart = Node()
    afterEnd = Node()

    while(chain):
        nex = chain.next
        chain.next = None               # Used so that we dont accidently create a circular linked list
        if chain.val < target:
            if beforeStart.val == None: # Kind of like a bool
                beforeStart = chain
                beforeEnd = beforeStart
            else:
                beforeEnd.next = chain
                beforeEnd = chain
        else:
            if afterStart.val == None:
                afterStart = chain
                afterEnd = afterStart
            else:
                afterEnd.next = chain
                afterEnd = chain
        chain = nex

    if not beforeStart:
        return afterStart

    beforeEnd.next = afterStart
    return beforeStart
            


if __name__ == "__main__":
    chain = list_to_linkedList([3,5,8,5,10,2,1])
    partition(chain.head, 5).print()
