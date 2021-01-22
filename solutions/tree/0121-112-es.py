# helper class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            if root.val == targetSum:
                return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

# test
if __name__ == '__main__':
    root = TreeNode(3)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    root.left = node1
    root.right = node2

    res = Solution().hasPathSum(root, 4)
    print(res)