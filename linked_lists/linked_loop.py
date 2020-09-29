from linkedList import LinkedList
from linkedList import Node
from linkedList import list_to_linkedList


def find_linked_loop(l: LinkedList) -> Node:
    visited = {}
    while(l):
        if l in visited:
            return True
        visited[l] = None
        l = l.next
            
    return False
