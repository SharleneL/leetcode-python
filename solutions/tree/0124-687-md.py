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
    cur_longest = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # self.cur_longest = 0
        longestPathThruRoot, longestPathInSubtrees = self.helper(root)
        return self.cur_longest

    # return [longestPathThruRoot, longestPathInSubtrees]
    def helper(self, root: TreeNode) -> []:
        if not root:
            return [0, 0]
        longestPathThruRootLeft, longestPathInSubtreesLeft = self.helper(root.left)
        longestPathThruRootRight, longestPathInSubtreesRight = self.helper(root.right)
        longestPathThruRootCur = 0
        longestPathInSubtreesCur = 0
        if (root.left and root.val == root.left.val) or (root.right and root.val == root.right.val):
            if (root.left and root.val == root.left.val) and (root.right and root.val == root.right.val):
                longestPathThruRootCur = max(longestPathThruRootLeft, longestPathThruRootRight) + 1
                self.cur_longest = max(self.cur_longest, longestPathThruRootLeft+longestPathThruRootRight)
            if root.left and root.val == root.left.val:
                longestPathThruRootCur = longestPathThruRootLeft + 1
            if root.right and root.val == root.right.val:
                longestPathThruRootCur = max(longestPathThruRootRight, longestPathThruRootRight + 1)
        longestPathInSubtreesCur = max(longestPathThruRootCur, longestPathInSubtreesLeft, longestPathInSubtreesRight)
        self.cur_longest = max(self.cur_longest, longestPathThruRootCur)
        return [longestPathThruRootCur, longestPathInSubtreesCur]


if __name__ == '__main__':
    root = TreeNode(1)
    R = TreeNode(1)
    root.right = R

    RL = TreeNode(1)
    RR = TreeNode(1)
    R.left = RL
    R.right = RR

    RLL = TreeNode(1)
    RLR = TreeNode(1)
    RL.left = RLL
    RL.right = RLR

    RRL = TreeNode(1)
    RR.left = RRL

    res = Solution().longestUnivaluePath(root)
    print(res)