def right_view(root):
    if root is None:
        return []
    right_view_nodes = []
    queue = [root]

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            if i == level_size - 1:
                right_view_nodes.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return right_view_nodes
