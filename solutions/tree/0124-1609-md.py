# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return False

        from collections import deque
        q = deque()
        cur = root
        q.append(cur)
        cur_level = 0
        while q:
            cur_level_size = len(q)
            isEvenLevel = cur_level % 2 == 0
            if isEvenLevel:  # odd + should increase
                prev_val = -sys.maxsize - 1
            else:
                prev_val = sys.maxsize

            for _ in range(cur_level_size):
                cur = q.popleft()
                # process
                if isEvenLevel:  # odd + should increase
                    if cur.val % 2 == 1 and cur.val > prev_val:
                        prev_val = cur.val
                    else:
                        return False
                else:
                    if cur.val % 2 == 0 and cur.val < prev_val:
                        prev_val = cur.val
                    else:
                        return False

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            cur_level += 1
        # end traversal
        return True


"""
definition:
- BT is EO if all applies
    - level starts from 0
    - even level: vals have odd & increase
    - odd level: vals have even & decrease

input:
- root
output:
- bool

---
have to traverse whole tree
BFS
"""