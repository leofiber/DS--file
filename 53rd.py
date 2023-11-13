class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def array_to_bst(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    for value in arr[1:]:
        insert(root, value)

    return root

# Example usage:
arr = [4, 2, 6, 1, 3, 5, 7]
root = array_to_bst(arr)
