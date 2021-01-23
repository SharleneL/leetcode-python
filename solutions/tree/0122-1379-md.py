# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or not cloned:
            return None

        # should both exist as it is guarenteed the 2 trees are cloned
        if original == target:
            return cloned
        targetLeft = self.getTargetCopy(original.left, cloned.left, target)
        targetRight = self.getTargetCopy(original.right, cloned.right, target)
        return targetLeft or targetRight


"""
input: 2 trees, cloned + a target node in T1
output: target in T2

traverse the tree till find target in 1
meanwhile do the same step for T2

dfs(root1, root2):
    if root1 == target:
        return root2
    resL = dfs(root1.left)
    resR = dfs(root1.right)
"""