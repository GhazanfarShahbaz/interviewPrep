from linkedList import LinkedList
from linkedList import Node
from linkedList import list_to_linkedList


def remove_element(chain: LinkedList, k: int, size=[0], curr=0):
    if chain:
        size[0] += 1
        n = curr + 1
        remove_element(chain.next, k, size, n)

        if(curr == size[0]-k-1):
            if k == 0:
                chain.next = None
            else:
                chain.next = chain.next.next

    if k == size[0] and curr == 0:
        chain = chain.next
    return chain


if __name__ == "__main__":
    chain = list_to_linkedList([1,2,3,4,5]).head
    chain = remove_element(chain, 1)
    chain.print()
