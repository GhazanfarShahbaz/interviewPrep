def createMinimalistTree(values: arr) -> Tree or None:
    if values:
        return createMinimalistTree(values, 0, len(arr)-1)
    return None

def createMinimalistTree(values:arr, start:int , end :int) -> None:
    middle = (start + end)//2

    tree = TreeNode(values[middle])
    tree.left = createMinimalistTree(values, start, middle-1)
    tree.right = createMinimalistTree(values, middle+1, end)
    return tree
