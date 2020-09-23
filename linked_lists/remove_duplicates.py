"""Challenge 2.1 Remove Dups
Write code to remove duplcates from an unsorted linked list?
How would you solve this problem if a temporary buffer is not allowed"""

from linkedList import Node
from linkedList import LinkedList
from linkedList import list_to_linkedList


def remove_duplicates(chain: LinkedList):
    """O(N) complexity"""
    if not chain.head:
        return
    values = {}
    parse = chain.head
    previous = None
    while(parse):
        if parse.val in values.keys():
            previous.next = parse.next
        else:
            values[parse.val] = 0
            previous = parse
        parse = parse.next

    # values = {chain.head.val: 0}
    # while(parse):
    #     if parse.val not in values.keys():
    #         values[parse.val] = 0
    #     if parse.next and parse.next.val not in values.keys():
    #         values[parse.next.val] = 0
    #     else:
    #         # parsing = parse
    #         # while parsing.next and parsing.next.val in values.keys():
    #         if parse.next and  parse.next.next:
    #             parse.next = parse.next.next
    #         else:
    #             parse.next = None
    #         # parsing.next = parsing.next.next
    #     parse = parse.next
    # # previousN = None
    # # while(chain):
    # #     if chain.val not in valyes


if __name__ == "__main__":  
    test = list_to_linkedList([1,1,11,1,1,1,2,2,2,2,2,3,4,56,7])
    test.print()
    remove_duplicates(test)

    test.print()
