def checkBalance(Tree):
    checkBalance(Tree.root)
    
def checkBalance(node):
    if node:
        checkBalance(node.left)
        checkBalance(node.right)
        if abs(getHeight(node.left, 0) - getHeight(node.right, 0)) > 1:
            return False
    return True

def getHeight(node, height):
    if(node):
        height += 1
        return max(getHeight(node.right, height ), getHeight(node.left,height))
    return height