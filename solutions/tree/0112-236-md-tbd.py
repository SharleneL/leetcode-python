class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        _, _, res = self.helper(root, p, q)
        return res

    def helper(self, root: TreeNode, p: TreeNode, q: TreeNode) -> []:
        contains_p = False
        contains_q = False
        lca_node = None
        if not root:
            return [contains_p, contains_q, lca_node]
        if root == p:
            contains_p = True
            return [contains_p, contains_q, lca_node]
        if root == q:
            contains_q = True
            return [contains_p, contains_q, lca_node]

        left_contains_p, left_contains_q, left_lca_node = self.helper(root.left, p, q)
        right_contains_p, right_contains_q, right_lca_node = self.helper(root.right, p, q)
        contains_p = left_contains_p or right_contains_p
        contains_q = left_contains_q or right_contains_q
        if left_lca_node:
            return [contains_p, contains_q, left_lca_node]
        elif right_lca_node:
            return [contains_p, contains_q, right_lca_node]
        else:
            if (left_contains_p and right_contains_q) or (left_contains_q and right_contains_p):
                return [True, True, root]
            else:
                return [contains_p, contains_q, None]
