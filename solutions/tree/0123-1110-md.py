# 如果从上往下（先处理parent再处理child）的话，有可能parent要被delete同时child也需要被delete，就不好办了
# 所以可以先处理child再处理parent。---> post order
# what to return: 因此递归函数应该返回的是以该root为根的subtree在delete node之后的结果
# what to do in cur level:
#     先得到左右孩子的处理结果 ->
#     然后处理自己：
#       如果root需要被delete的话，return None，同时把孩子们返回的结果放到forest里面。这里注意孩子们返回的结果有可能为None，要判断非空之后才append。
#       如果root不需要delete的话，将root.left和root.right设为孩子们返回的结果

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        forest = []
        if not root:
            return forest
        new_root = self.dfs(root, to_delete, forest)
        if new_root:
            forest.append(new_root)
        return forest

    def dfs(self, root: TreeNode, to_delete: List[int], forest: List[TreeNode]) -> TreeNode:
        if not root:
            return None
        # 先处理children最后处理自己，这样可以保证subtree里面已经没有要delete的
        leftNode = self.dfs(root.left, to_delete, forest)
        # if leftNode
        rightNode = self.dfs(root.right, to_delete, forest)

        # deal with itself
        if root.val in to_delete:
            to_delete.remove(root.val)
            # add children to res
            if leftNode:
                forest.append(leftNode)
            if rightNode:
                forest.append(rightNode)
            return None
        else:
            root.left = leftNode
            root.right = rightNode
            return root