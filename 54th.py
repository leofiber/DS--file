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

def delete_from_bst(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = delete_from_bst(root.left, key)
    elif key > root.value:
        root.right = delete_from_bst(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        root.value = find_min(root.right).value
        root.right = delete_from_bst(root.right, root.value)

    return root

def find_min(node):
    while node.left:
        node = node.left
    return node
