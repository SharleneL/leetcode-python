# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total_count = 0

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.dfs(root, root.val)
        return self.total_count

    def dfs(self, root: TreeNode, maxPrevVal: int):
        if not root:
            return
        if maxPrevVal <= root.val:
            self.total_count += 1
            maxPrevVal = max(maxPrevVal, root.val)
        self.dfs(root.left, maxPrevVal)
        self.dfs(root.right, maxPrevVal)