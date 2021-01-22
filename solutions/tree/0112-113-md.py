# 要点：如果topdown并且pass down东西的话，切记我们每一层用的这个passdoen的东西都是同一个obj
# - 因此curPath需要copy之后再append到res里面
# - 因此curPath需要pop

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        self.helper(root, targetSum, [], res)
        return res

    def helper(self, root: TreeNode, targetSum: int, curPath: List[int], res: List[List[int]]):
        if not root:
            return

        curPath.append(root.val)
        if not root.left and not root.right:
            if root.val == targetSum:
                res.append(curPath.copy()) # IMPORTANT: need to make a copy, o/w when curPath pops, the path inside res will be changed as well.
            curPath.pop()
            return
        else:
            self.helper(root.left, targetSum - root.val, curPath, res)
            self.helper(root.right, targetSum - root.val, curPath, res)
            curPath.pop() # IMPORTANT: must pop after current level is processed, coz curPath need to be passed down from its current parent to sibling

# test
if __name__ == '__main__':
    root = TreeNode(5)
    n4 = TreeNode(4)
    n8 = TreeNode(8)
    root.left = n4
    root.right = n8

    res = Solution().pathSum(root, 9)
    print(res)