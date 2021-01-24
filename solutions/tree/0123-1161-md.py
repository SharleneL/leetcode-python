class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        from collections import deque
        q = deque()
        q.append(root)  # [1]
        level_sums = []  # []
        while q:
            cur_level_size = len(q)  # 1
            cur_level_sum = 0
            # print(len(q))
            for _ in range(cur_level_size):  # 1
                cur = q.popleft()  # 注意！！！是popleft！！不是pop！！！
                # print('# ' + str(cur.val))
                cur_level_sum += cur.val  # 0+1
                if cur.left:
                    q.append(cur.left)  # [7]
                if cur.right:
                    q.append(cur.right)  # [7. 0]
            level_sums.append(cur_level_sum)  # [1]
        max_sum = max(level_sums)
        max_level = level_sums.index(max_sum) + 1

        return max_level

if __name__ == '__main__':
    root = TreeNode(989)
    node2 = TreeNode(10250)
    node21 = TreeNode(98693)
    node22 = TreeNode(-89388)
    node222 = TreeNode(-32127)
    root.right = node2
    node2.left = node21
    node2.right = node22
    node22.right = node222

    res = Solution().maxLevelSum(root)
    print(res)