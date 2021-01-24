# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def convertBST(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return root

#         stack = []
#         cur = root
#         stack.append(root)
#         cur_sum = 0
#         while stack or cur:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.right
#             cur = stack.pop() # most right
#             cur_sum += cur.val
#             cur.val = cur_sum
#             cur = cur.left # is None
#         return root
"""
input: root BST
output:
-> greater tree; val -> val+sum(all keys > original)

in order can get the max->min sequence, but right->root->left
use a cur_sum to log the sum of all bigger numbers sum
"""


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)

        total = 0
        dfs(root)
        return root