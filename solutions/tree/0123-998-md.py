'''
其实就是找规律
如果插入值比根val大，则新建一个node并把root放到new node的左边（因为new val是append到arr的最右）
如果插入值比根val小，则向右走（因为new val是append到arr的最右）并且重复上述步骤
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        return self.helper(root, val)

    def helper(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            new_node = TreeNode(val)
            return new_node
        if root.val < val:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node
        else:
            root.right = self.helper(root.right, val)
            return root

