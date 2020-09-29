from linkedList import LinkedList
from linkedList import Node
from linkedList import list_to_linkedList


def delete_middle(chain: LinkedList, size=[0], curr=0): # This is just to get the middle node : the helper function isnt needed
    if chain:
        size[0] += 1
        delete_middle(chain.next, size, curr+1)
        if curr == int(size[0]/2):
            delete_middle_given_middle(chain)
            # chain.next = chain.next.next

def delete_middle_given_middle(chain: LinkedList):
    if chain.next == None or not chain:
        return

    chain.val = chain.next.val
    chain.next = chain.next.next

if __name__ == "__main__":
    s = list_to_linkedList([1,2,3,4,5]).head
    delete_middle(s)
    s.print()
 