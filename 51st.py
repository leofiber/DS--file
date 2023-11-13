def left_view(root):
    if root is None:
        return []
    left_view_nodes = []
    queue = [root]

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            if i == 0:
                left_view_nodes.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return left_view_nodes