def postorder_to_preorder(postorder):
    if not postorder:
        return []

    root_val = postorder[-1]
    postorder.pop()

    if not postorder:
        return [root_val]

    left_postorder = []
    right_postorder = []

    for val in postorder:
        if val < root_val:
            left_postorder.append(val)
        else:
            right_postorder.append(val)

    left_preorder = postorder_to_preorder(left_postorder)
    right_preorder = postorder_to_preorder(right_postorder)

    return [root_val] + left_preorder + right_preorder

postorder = [35, 30, 100, 80, 40]
preorder = postorder_to_preorder(postorder)
print(preorder)
