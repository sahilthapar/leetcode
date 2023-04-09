class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(root: TreeNode,
                           p: TreeNode,
                           q: TreeNode) -> TreeNode:
    # if both are split
    if (p.val <= root.val <= q.val) or (p.val >= root.val >= q.val):
        return root

    # if both are lower, search the left side
    if p.val <= root.val and q.val <= root.val:
        return lowest_common_ancestor(root.left, p, q)

    # if both are higher, search the right side
    else:
        return lowest_common_ancestor(root.right, p, q)
