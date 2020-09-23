class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        # Obvi this is just for my own use, size is very inefficient because it will only give you correct size for the head every other value will simply signify how many elements are left
        self.size = 1
        if self.next:
            self.size = self.next.size + 1


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        parse = self.head
        string = ""
        while(parse):
            # print(parse.val)
            string += f"{parse.val} "
            parse = parse.next
        print(string)

def list_to_linkedList(arr: list) -> LinkedList:
    linked = LinkedList()

    for x in range(len(arr)-1, -1, -1):
        curr = Node(arr[x], linked.head)
        linked.head = curr
    
    return linked


if __name__ == "__main__":
    print("Nothing here")