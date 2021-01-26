# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder or not inorder:
            return None

        cur_root_val = postorder[-1]
        cur_root = TreeNode(cur_root_val)

        cur_root_inorder_idx = inorder.index(cur_root_val)
        inorder_left = inorder[:cur_root_inorder_idx]
        inorder_right = inorder[cur_root_inorder_idx + 1:]
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):-1]

        cur_root.left = self.buildTree(inorder_left, postorder_left)
        cur_root.right = self.buildTree(inorder_right, postorder_right)

        return cur_root

if __name__ == '__main__':
    res = Solution().buildTree([9,3,15,20,7], [9,15,7,20,3])

    print(1)
    print(res)