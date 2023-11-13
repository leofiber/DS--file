class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder_to_postorder(preorder):
    if not preorder:
        return []

    root_val = preorder[0]
    preorder.pop(0)

    if not preorder:
        return [root_val]

    left_preorder = []
    right_preorder = []

    for val in preorder:
        if val < root_val:
            left_preorder.append(val)
        else:
            right_preorder.append(val)

    left_postorder = preorder_to_postorder(left_preorder)
    right_postorder = preorder_to_postorder(right_preorder)

    return left_postorder + right_postorder + [root_val]

preorder = [40, 30, 35, 80, 100]
postorder = preorder_to_postorder(preorder)
print(postorder)
