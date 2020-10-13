def validateBST(Tree):
    return check(Tree.root)

def checkTree(root, minN = None, maxN = None):
    if root:
        if((minN != None and root.val <= minN) or (maxN != None and root.val >= maxN)):
            return False
        if(not checkTree(root.left, minN, root.val) or not checkTree(root.right, root.val, maxN):
            return False
    return True
