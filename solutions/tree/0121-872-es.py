class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leftLeafNodes = []
        rightLeafNodes = []
        self.helper(root1, leftLeafNodes)
        self.helper(root2, rightLeafNodes)
        return leftLeafNodes == rightLeafNodes

    def helper(self, root: TreeNode, leafNodes: List[int]):
        if not root:
            return leafNodes
        if not root.left and not root.right:
            leafNodes.append(root.val)

        self.helper(root.left, leafNodes)
        self.helper(root.right, leafNodes)