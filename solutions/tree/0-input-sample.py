from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    root = TreeNode(2)
    node11 = TreeNode(1)
    node12 = TreeNode(1)
    node21 = TreeNode(1)
    node22 = TreeNode(3)
    node31 = TreeNode(1)
    root.left = node11
    root.right = node12
    node11.left = node21
    node11.right = node22
    node22.right = node31

    res = Solution().pseudoPalindromicPaths(root)
    print(res)

    print(Solution().isPal([1, 1, 2, 3]))