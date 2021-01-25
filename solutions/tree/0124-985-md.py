# 每层返回什么？
# 返回当前节点向下延伸的最长长度
# 每一层做什么？
# check左右的返回值并用返回值update class variable（self.cur_longest）

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            cur_level_size = len(q)
            cur_level_contains_none = False
            for _ in range(cur_level_size):
                cur = q.popleft()
                if not cur:
                    # if cur is None, rest of the elems must ALL be none
                    cur_level_contains_none = True
                else:
                    if cur_level_contains_none:
                        return False
                    else:
                        q.append(cur.left)
                        q.append(cur.right)
            # end while
        return True


if __name__ == '__main__':
    R = TreeNode(1)
    RL = TreeNode(2)
    RR = TreeNode(3)
    R.left = RL
    R.right = RR

    RLL = TreeNode(4)
    RLR = TreeNode(5)
    RRL = TreeNode(6)
    RRR = TreeNode(7)
    RL.left = RLL
    # RL.right = RLR
    RR.left = RRL
    # RR.right = RRR

    # RLLL = TreeNode(8)
    RLLR = TreeNode(9)
    # RLL.left = RLLL
    RLL.right = RLLR
    # RLRL = TreeNode(10)
    # RLRR = TreeNode(11)
    # RLR.left = RLRL
    # RLR.right = RLRR
    # RRLL = TreeNode(12)
    # RRLR = TreeNode(13)
    # RRL.left = RRLL
    # RRL.right = RRLR
    # # RRRL = TreeNode(1)
    # # RRRR = TreeNode(1)
    # RLLLL = TreeNode(15)
    # RLLL.left = RLLL
    # # RR.left = RRL

    res = Solution().isCompleteTree(R)
    print(res)