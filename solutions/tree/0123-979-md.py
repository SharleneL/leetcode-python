'''
我智商还可以嘛。。。
看题第一眼第一反应是topdown怎么搞（如何从整个树的角度来balance）
但是应该考虑breakup into small problems，关注单一节点：
- 对于某一个节点，它【需要】或者可以【给予】什么？
- 对于某一个子树，它作为一个整体【需要】或者可以【给予】什么？它的【内部】需要怎么样才可以balance？

所以可以想到：
- 定义一个overload value，表示某个节点在balance了自己的子孙之后可以向上提供的资源（>0则可以给别人用，<0则从别人那里拿）
- 给我一个subtree的root，我让它的子孙们全都balance，子孙们欠的债全都体现在这个root的overload value上
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total_move = 0

    def distributeCoins(self, root: TreeNode) -> int:
        if not root:
            return self.total_move

        self.calOverload(root)
        return self.total_move

    def calOverload(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 如果是leaf node，只要平衡自己就可以了，>0表示多出来的value可以给别人，<0表示需要向parent借钱来balance自己
        if not root.left and not root.right:
            return root.val - 1  # how many coins are extra(if >0) OR needs to borrow(if <0)?

        # if not leaf node, balance cur subtree with moves
        left_overload = self.calOverload(root.left)
        right_overload = self.calOverload(root.right)
        # balance左右子树所需要的move数 - 如果left overload了3，则证明需要从left拿走3个它才会balance。right同理
        left_moves = left_overload  # if>0, means move to parent; if <0, means borrow from parent
        right_moves = right_overload  # if>0, means move to parent; if <0, means borrow from parent
        # 将balance当前subtree左右子树的move加入到总move数里面。注意要abs。
        self.total_move = self.total_move + abs(left_moves) + abs(right_moves)
        # 计算当前层的overload。因为要留一个coin给自己所以要-1
        cur_overload = root.val + left_overload + right_overload - 1
        return cur_overload


"""
input: 
- root: n nodes; each has .val coins; total n coins (sum of nodes# == sum of val)

definition:
- move: 1 -> another; p>ch or ch>p

output:
- # moves, each node has 1 coin
"""
