# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    recovered_root = None

    def __init__(self, root: TreeNode):
        # recover the tree
        if not root:
            return

        def recover(root: TreeNode, parentVal: int, isLeft: bool):
            if not root:
                return
            if isLeft:
                root.val = parentVal * 2 + 1
            else:
                root.val = parentVal * 2 + 2
            recover(root.left, root.val, True)
            recover(root.right, root.val, False)

        cur = root
        cur.val = 0
        recover(root.left, 0, True)
        recover(root.right, 0, False)
        self.recovered_root = root

    def find(self, target: int) -> bool:
        # find the target
        def helper(target: int, root: TreeNode) -> bool:
            if not root:
                return False
            if target == root.val:
                return True
            if target < root.val * 2 + 1:
                return False
            return helper(target, root.left) or helper(target, root.right)

        return helper(target, self.recovered_root)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)


"""
input: BTree root
    root=0
    val=x, leftVal=2x+1, rightVal=2x+2
"contaminated": all treeval=-1

recover tree + FindElements(root)

# test cases
obj = FindElements(root) -> then root will be recovered

obj.find(target) -> then 

"""