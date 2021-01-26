# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post:
            return None

        cur_root_val = pre[0]
        cur_root = TreeNode(cur_root_val)

        if len(pre) == 1:
            return cur_root

        left_root_val = pre[1]
        left_root_post_idx = post.index(left_root_val)  # 2
        post_left = post[:left_root_post_idx + 1]  # 【452】
        post_right = post[left_root_post_idx + 1:-1]  # 637
        pre_left = pre[1:left_root_post_idx + 2]  # 24
        pre_right = pre[left_root_post_idx + 2:]

        cur_root.left = self.constructFromPrePost(pre_left, post_left)
        cur_root.right = self.constructFromPrePost(pre_right, post_right)
        return cur_root