# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        evenNodes = []
        if not root:
            return evenNodes

        from collections import deque
        q = deque()
        q.append(root)
        while q:
            cur_level_size = len(q)
            for _ in range(cur_level_size):
                cur = q.popleft()
                if cur.val % 2 == 0:
                    evenNodes.append(cur)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        res = []
        for even_node in evenNodes:
            if even_node.left:
                if even_node.left.left:
                    res.append(even_node.left.left.val)
                if even_node.left.right:
                    res.append(even_node.left.right.val)
            if even_node.right:
                if even_node.right.left:
                    res.append(even_node.right.left.val)
                if even_node.right.right:
                    res.append(even_node.right.right.val)
        return sum(res)