# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_diff = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return self.max_diff
        # TODO: call helper
        self.dfs(root, root.val, root.val)
        return self.max_diff

    def dfs(self, root: TreeNode, cur_path_max: int, cur_path_min: int):
        if not root:
            return

        cur_path_max = max(cur_path_max, root.val)
        cur_path_min = min(cur_path_min, root.val)
        if not root.left and not root.right:
            self.max_diff = max(self.max_diff, cur_path_max - cur_path_min)
        else:
            self.dfs(root.left, cur_path_max, cur_path_min)
            self.dfs(root.right, cur_path_max, cur_path_min)


"""
input: 
- root
output:
- maxVal of V, V=abs(A.val - B.val) && A>B
absDiff(ancestor, child) -> find max

find each pair of <ancestor, child> - then max

need to traverse ALL tree
BFS? no
DFS - get max diff of each path
    - record min + max of each path, when reach the bottom, cal the diff

-> path problem
"""