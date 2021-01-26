# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # return root of cur subtree
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        cur_root_val = preorder[0]
        cur_root = TreeNode(cur_root_val)

        cur_root_inorder_idx = inorder.index(cur_root_val)  # 1
        inorder_left = inorder[:cur_root_inorder_idx]  # [9]
        inorder_right = inorder[cur_root_inorder_idx + 1:]  # [15.20.7]
        preorder_left = preorder[1:1 + len(inorder_left)]  # []
        preorder_right = preorder[1 + len(inorder_left):]

        cur_root.left = self.buildTree(preorder_left, inorder_left)
        cur_root.right = self.buildTree(preorder_right, inorder_right)

        return cur_root
