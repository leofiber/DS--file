class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def top_view(root):
    if not root:
        return

    horizontal_distance = 0
    hd_dict = {}
    queue = [(root, horizontal_distance)]
    min_hd = float('inf')
    max_hd = -float('inf')

    while queue:
        node, hd = queue.pop(0)
        if hd < min_hd:
            min_hd = hd
            hd_dict[hd] = node.data
        if hd > max_hd:
            max_hd = hd
            hd_dict[hd] = node.data
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    top_view_nodes = [hd_dict[hd] for hd in range(min_hd, max_hd + 1)]
    return top_view_nodes

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)
root.left.right.right.right = TreeNode(6)

print("Top View:", top_view(root))
