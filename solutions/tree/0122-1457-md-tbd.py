# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    totalNum = 0

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if not root:
            return self.totalNum
        path = []
        self.dfs(root, path)
        return self.totalNum

    def dfs(self, root: TreeNode, path: List[int]):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            if self.isPal(path):
                self.totalNum += 1
            path.pop()
        else:
            self.dfs(root.left, path)
            self.dfs(root.right, path)
            path.pop()

    def isPal(self, path: List[int]) -> bool:
        if not path:
            return False
        p = path.copy()
        p.sort()
        stack = []
        for val in p:
            if not stack:
                stack.append(val)
            else:
                if stack[-1] == val:
                    stack.pop()
                else:
                    stack.append(val)
        if len(stack) <= 1:
            return True
        return False

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

"""
dfs all the paths
have a helper check if the path is palindrom permutation
"""