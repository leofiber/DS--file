def lowestCommonAncestor(root, p, q):
    if root is None:
        return None

    if root.val==p.val or root.val==q.val:
        return root

    left_lca=lowestCommonAncestor(root.left,p,q)
    right_lca=lowestCommonAncestor(root.right,p,q)

    if left_lca !=None and right_lca!=None:
        return root

    if left_lca!=None:
        return left_lca
    return right_lca

        
