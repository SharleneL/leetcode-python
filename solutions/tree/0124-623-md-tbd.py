"""
我的解法：
使用tuple来处理nodes
但是没过，因为似乎无法handle在最低一层加一行的情况

比如input:
[1,2,3,4]
5
4

不想debug了。。。
"""
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root:
            return root
        self.helper(root, True, v, d)
        return root

    def helper(self, root: TreeNode, isLeftOfParent: bool, v: int, d: int):
        from collections import deque
        q = deque()
        if not root:
            return
        q.append((root, isLeftOfParent))
        cur_depth = 1
        while q:
            is_target_depth = d==cur_depth
            cur_level_size = len(q)
            for _ in range(cur_level_size):
                cur, curIsLeftOfParent = q.popleft()
                if is_target_depth:
                    original_cur = TreeNode(cur.val)
                    original_cur.left = cur.left
                    original_cur.right = cur.right
                    cur.val = v
                    if curIsLeftOfParent:
                        cur.left = original_cur
                        cur.right = None
                    else:
                        cur.right = original_cur
                        cur.left = None
                else:
                    if cur.left:
                        q.append((cur.left, True))
                    if cur.right:
                        q.append((cur.right, False))
            cur_depth += 1

"""
input:
- root
- v - int
- d - int, depth

todo:
- add a row of nodes with val=v at depth=d; root's depth==1

output:
- treenode of new root

rule:
- at depth=d, each nonNull node N in depth d-1

---
BFS, find depth=d's all nodes (rootDepth=1)
for curNode at depth=d:
    originalCur = TreeNode(curNode.val)
    originalCur.left = curNode.left
    originalCur.right = curNode.right
    curNode.val = val
    if isLeftOfParent:
        curNode.left = originalCur
        curNode.right = None
    else:
        .right =
        .left = None

"""