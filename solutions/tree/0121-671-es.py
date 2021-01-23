# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method1: top down
# [pass the res value down] from the top level caller -> DFS traversal -> change the res value while traversing
# Notice: the passed down value needs to be class value. O/w it would be local variable and will only exist in called function but not reflected in the initial caller.
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.first = root.val
        self.second = sys.maxsize
        self.helper(root)
        if self.second == sys.maxsize:
            return -1
        else:
            return self.second

    def helper(self, root: TreeNode):
        if not root:
            return

        # DO NOT NEED coz root <= children
        # if root.val < self.first:
        #     self.second = self.first
        #     self.first = root.val
        #     self.helper(root.left)
        #     self.helper(root.right)
        if root.val == self.first:
            self.helper(root.left)
            self.helper(root.right)
        elif root.val < self.second:
            self.second = root.val
            self.helper(root.left)
            self.helper(root.right)
        else:
            return


# Method2: bottom-up
# [return res val] at each level
# Notice: think about what shall be returned for each level?
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        return self.helper(root, root.val)

    # this helper finds the smallest val > first, starting from root node
    def helper(self, root: TreeNode, first) -> int:
        if not root:
            return -1
        if root.val != first:  # means cur root is the most recent val which > first
            return root.val

        # if == first, continue check left + right
        left = self.helper(root.left, first)
        right = self.helper(root.right, first)
        if (left == -1 or right == -1):  # means no res from 1 or 2 sides
            return max(left, right)
        else:  # means get 2 vals from each side
            return min(left, right)
