class linkedList:
    def __init__(self, node = None):
        self.head = Node()
    def insert(seld, node):
        parse = seld.head
        while(parse.next):
            parse = parse.next
        parse.next = noe
class Node:
    def __init__(self):
        self.val = None
        self.next = None
    def __init__(self, val , nextN = None):
        self.val = val
        self.next = nextN


def listOfDepths(Tree):
    depthList = []
    listOfDepths(tree, 0, depthList)
    return depthList

def listOfDepths(node, depth, depthList):
    if node:
        if len(someList) == depth:
            depthList.append(linkedList(Node(node.val)))
        else:
            depthList[depth].insert(node)
        depth += 1
        listOfDepths(node.right, depth, depthList)
        listOfDepths(node.left, depth, depthList)