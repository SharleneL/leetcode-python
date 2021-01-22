class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = []
        self.midOrder(root, res)
        if len(res) < 2:
            return 0
        minDif = sys.maxsize
        for i in range(1, len(res)):
            minDif = min(minDif, abs(res[i - 1] - res[i]))
        return minDif

    def midOrder(self, root: TreeNode, res: int) -> int:
        if not root:
            return res
        self.midOrder(root.left, res)
        res.append(root.val)
        self.midOrder(root.right, res)