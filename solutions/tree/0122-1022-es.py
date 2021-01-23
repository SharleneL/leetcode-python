# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 定义一个class variable
    res = 0

    def sumRootToLeaf(self, root: TreeNode) -> int:
        # self.res = 0 # 或者定义在这里也行

        self.helper(root, 0)
        return self.res

    # if reach to leaf, add it into res
    def helper(self, root: TreeNode, curVal):
        if not root:
            return
        curVal = curVal * 2 + root.val  # 位运算
        if not root.left and not root.right:
            self.res += curVal
        else:
            self.helper(root.left, curVal)
            self.helper(root.right, curVal)