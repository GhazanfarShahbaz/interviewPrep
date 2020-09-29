from linkedList import LinkedList
from linkedList import Node
from linkedList import list_to_linkedList


def traverseByDifference(node: LinkedList, difference: int) -> Node:
    for x in range(difference):
        node = node.next

    return node


def intersection(listOne: LinkedList, listTwo: LinkedList) -> Node or None:
    if (listOne.head and not listTwo.head) or (not listOne.head and listTwo.head):
        return False
    elif not listOne.head and not listTwo.head:
        return None

    nodeOne = listOne.head
    nodeTwo = listTwo.head

    if nodeOne.size > nodeTwo.size:
        nodeOne = traverseByDifference(nodeOne, nodeOne.size - nodeTwo.size)
    elif nodeOne.size < nodeTwo.size:
        nodeTwo = traverseByDifference(nodeTwo, nodeTwo.size - nodeOne.size)

    while(nodeOne and nodeOne.val != nodeTwo.val):
        nodeOne = nodeOne.next
        nodeTwo = nodeTwo.next

    return nodeOne


if __name__ == "__main__":
    t = list_to_linkedList([8,9])
    t2 = list_to_linkedList([2,7,8,9])

    intersection(t, t2).print()