# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        last_level_sum = 0
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            cur_level_size = len(q)
            cur_level_sum = 0
            for _ in range(cur_level_size):
                cur = q.popleft()
                cur_level_sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            last_level_sum = cur_level_sum
        return last_level_sum