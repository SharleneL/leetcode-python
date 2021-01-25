"""
注意最后的max len不一定通过root
如果题目中说"不一定通过root"的最值的话，往往需要维护一个*全局变量*!!!
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None, name=None):
        self.val = val
        self.left = left
        self.right = right
        self.name = name


#         self.right = right
class Solution:
    longest = 0

    def longestZigZag(self, root: TreeNode) -> int:
        self.helper(root)
        return self.longest

    # return [longest_z_len_if_go_left, longest_z_len_if_go_right]
    def helper(self, root: TreeNode) -> []:
        if not root:
            return [-1, -1]
        _, left_longest_go_right = self.helper(root.left)
        right_longest_go_left, _ = self.helper(root.right)
        cur_longest_go_left = 1 + left_longest_go_right
        cur_longest_go_right = 1 + right_longest_go_left
        self.longest = max(self.longest, cur_longest_go_left, cur_longest_go_right)
        return [cur_longest_go_left, cur_longest_go_right]


"""
input:
- root

definition:
- zz path: 
- zz len: num of nodes along the path - 1 (aka ==edges)

output:
- longest zz len

---
need to traverse the tree
what should return from cur level?
- longest zz len if go left
- longest zz len if go right
what to do?
- 1+longestLeft(right) -> right
- 1+longestRight(left) -> left
"""

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