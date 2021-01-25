# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 抄答案
# 这个collections.defaultdict似乎很好用的样子
class Solution(object):
    def verticalTraversal(self, root):
        seen = collections.defaultdict(
            lambda: collections.defaultdict(list))

        def dfs(node, x=0, y=0):
            if node:
                seen[x][y].append(node)
                dfs(node.left, x - 1, y + 1)
                dfs(node.right, x + 1, y + 1)

        dfs(root)
        ans = []

        for x in sorted(seen):
            report = []
            for y in sorted(seen[x]):
                report.extend(sorted(node.val for node in seen[x][y]))
            ans.append(report)

        return ans


# class Solution:
#     index_to_vals = dict()
#     def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
#         self.index_to_vals = dict()
#         # first index is col, second index is depth
#         self.inOrder(root, 0, 1)
#         if not self.index_to_vals:
#             return []

#         def getDepth(tp):
#             return tp[1]
#         index_list = sorted(self.index_to_vals.keys())
#         res = []
#         for i in index_list:
#             tuple_res = sorted(self.index_to_vals[i], key=getDepth)
#             cur_res = []
#             for val, _ in tuple_res:
#                 cur_res.append(val)
#             res.append(cur_res)

#         return res

#     def inOrder(self, root: TreeNode, curCol: int, curDepth):
#         if not root:
#             return
#         # process cur
#         if curCol in self.index_to_vals:
#             self.index_to_vals[curCol].append((root.val, curDepth))
#         else:
#             self.index_to_vals[curCol] = [root.val]
#         # process left
#         self.inOrder(root.left, curCol-1, curDepth+1)
#         # process right
#         self.inOrder(root.right, curCol+1, curDepth+1)

"""
Need to traverse the whole tree
Need to know the 
inOrder traversal
    give index for each node: go left then -1; go right then +1
    add the node into a map
"""