class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_into_bst(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

def search_in_bst(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    if target < root.value:
        return search_in_bst(root.left, target)
    return search_in_bst(root.right, target)
