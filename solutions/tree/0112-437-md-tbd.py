# 最开始不work是因为如果把totalNum passdown的话，这个变量是局域性的，所以跳出函数之后totalNum不会被改变

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        totalNum = 0
        if not root:
            return totalNum

        self.helper(root, sum, totalNum)
        return totalNum

    def helper(self, root: TreeNode, sum: int, totalNum: int):
        if not root:
            return
        sum -= root.val
        if not root.left and not root.right:
            if sum == 0:
                totalNum += 1
        else:
            self.helper(root.left, sum, totalNum)
            self.helper(root.right, sum, totalNum)
        sum += root.val


# test
if __name__ == '__main__':
    root = TreeNode(5)
    n4 = TreeNode(4)
    n8 = TreeNode(8)
    root.left = n4
    root.right = n8

    res = Solution().pathSum(root, 9)
    print(res)