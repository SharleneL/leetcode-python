# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归的解法：
# 最基本：直接想到inorder遍历整个tree，得到一个list然后找第k个
# 进一步：其实没有必要遍历完，只要遍历到第k个数字就可以了。因此可以在inorder处理的时候check res的长度，到第k个的时候return即可。此时return，上一个level的len(res)==k也成立，因此可以一路返回到最上面。
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        self.inOrder(root, res, k)
        return res[k - 1]  # coz k is always valid

    def inOrder(self, root: TreeNode, res: List[int], k: int):
        if not root:
            return
        self.inOrder(root.left, res, k)
        if len(res) == k:
            return
        res.append(root.val)
        self.inOrder(root.right, res, k)


# 迭代的解法：
# 手动搞一个stack出来，inorder迭代traversal，因为是从最左最小开始遍历，所以可以遍历了一个元素就k-1。等到k为0的时候就证明找到了第k个。
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur = root
        stack.append(cur)
        while stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right