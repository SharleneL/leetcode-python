# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        res_map = dict()
        if not root:
            return []

        self.dfs(root, res_map)
        max_occ = 0
        res = []
        for val, occ in res_map.items():
            if occ > max_occ:
                max_occ = occ
                res = [val]
            elif occ == max_occ:
                res.append(val)
            else:
                next
        return res

    def dfs(self, root: TreeNode, res_map) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            if root.val in res_map:
                res_map[root.val] += 1
            else:
                res_map[root.val] = 1
            return root.val
        else:
            cur_sum = root.val + self.dfs(root.left, res_map) + self.dfs(root.right, res_map)
            if cur_sum in res_map:
                res_map[cur_sum] += 1
            else:
                res_map[cur_sum] = 1
            return cur_sum


"""
each subtree return the val of cur subtree's sum
when calc subtree sum, put it into a map<val, occ>
"""