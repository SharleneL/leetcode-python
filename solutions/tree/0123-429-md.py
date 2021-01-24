"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res

        from collections import deque
        q = deque()
        q.append(root)
        while q:
            cur_level_size = len(q)
            cur_level_res = []
            for _ in range(cur_level_size):
                cur = q.popleft()
                cur_level_res.append(cur.val)
                for child in cur.children:
                    q.append(child)
            res.append(cur_level_res)

        return res
