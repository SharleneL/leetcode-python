# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        max_width = 0
        if not root:
            return max_width

        from collections import deque
        q = deque()
        q.append((root, 1))
        while q:  # [1]
            cur_level_size = len(q)  # 1
            for i in range(cur_level_size):
                cur, cur_index = q.popleft()
                if i == 0:
                    cur_level_first_index = cur_index  # 1
                if i == cur_level_size - 1:
                    cur_level_last_index = cur_index  # 1
                if cur.left:
                    q.append((cur.left, cur_index * 2 - 1))
                if cur.right:
                    q.append((cur.right, cur_index * 2))
            max_width = max(max_width, cur_level_last_index - cur_level_first_index + 1)
        return max_width


"""
keep an index for each node
root index = 1
parent.left.index = parentIndex * 2 - 1
parent.right.index = parentIndex * 2
"""