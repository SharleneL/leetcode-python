from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None, name=None):
        self.val = val
        self.left = left
        self.right = right
        self.name = name


if __name__ == '__main__':
    root = TreeNode(1)
    R = TreeNode(1)
    R.name = "R"
    root.right = R

    RL = TreeNode(1)
    RL.name = "RL"
    RR = TreeNode(1)
    RR.name = "RR"
    R.left = RL
    R.right = RR

    RRL = TreeNode(1)
    RRL.name = "RRL"
    RRR = TreeNode(1)
    RRR.name = "RRR"
    RR.left = RRL
    RR.right = RRR

    RRLR = TreeNode(1)
    RRLR.name = "RRLR"
    RRL.right = RRLR

    RRLRR = TreeNode(1)
    RRLRR.name = "RRLRR"
    RRLR.right = RRLRR

    res = Solution().longestZigZag(root)
    print(res)