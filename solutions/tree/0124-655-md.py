"""
思路：
1. 找规律：创建一个m行的array，每行有n个元素 - m是树的depth（start from 1），且n=2^m-1
2. 从root开始，递归填入数字：
    - root放到第一行[0, 2^m-2]的中间index，即res[0][midIndex] (其中midIndex = (2^m-2)/2)
    - 递归left：将root.left.val放到第二行 [0, (上一层midIndex-1)]的中间index
    - 递归right：将root.left.val放到第二行 [(上一层midIndex+1), end]的中间index
    - 重复
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:


"""
need traversal: BFS might be better
need to know depth of the tree
"""