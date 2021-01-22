class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = []
        self.dfs(root, res)
        if len(res) < 2:
            return -1
        else:
            return res[1]

    def dfs(self, root: TreeNode, res: List[int]):
        if not root:
            return

        if len(res) == 0:
            res.append(root.val)
        elif len(res) == 1:
            if root.val != res[0]:
                res.append(root.val)
                res.sort()
        elif len(res) == 2:
            return

        if not root.left and not root.right:
            return
        elif not root.left:
            self.dfs(root.left, res)
        elif not root.right:
            self.dfs(root.right, res)
        else:
            if root.left.val < root.right.val:
                self.dfs(root.left, res)
            else:
                self.dfs(root.right, res)