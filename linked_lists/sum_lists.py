from linkedList import LinkedList
from linkedList import Node
from linkedList import list_to_linkedList

listOne = list_to_linkedList([7,1,6])
listTwo = list_to_linkedList([5,9,2])

def list_to_string(l: Node) -> str:
    string = ""
    while(l):
        string = f"{l.val}{string}"
        l = l.next
    return string

def sum_list(l1: LinkedList, l2: LinkedList) -> LinkedList or None:
    if not l1 and not l2:
        return None
    elif not l1:
        return l2
    elif not l2:
        return l1

    sum_of_list = str(int(list_to_string(l1.head)) + int(list_to_string(l2.head)))
    linkedSum = LinkedList()

    for x in range(0, len(sum_of_list)):
        curr = Node(sum_of_list[x], linkedSum.head)
        linkedSum.head = curr

    return linkedSum

if __name__ == "__main__":
    # print(list_to_string(listOne.head))
    sum_list(listOne, listTwo).print()
    