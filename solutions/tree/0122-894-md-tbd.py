# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N = 0:
            return [None]
        if N = 1:
            return [TreeNode(0)]

        for i in range(N / 2):
            leftRes = self.allPossibleFBT(i)
            rightRes = self.allPossibleFBT(N - i - 1)


"""
def: full BTree - either 0 or 2 child

input: N (node#)
output: list[possible FBTree's root node]

e.g.
- N = 1:
1

- N = 2:
0

- N = 3:
1
[0, 1, 2] - left=1, right=0
[2, 1, 0] - ^
[1, 1, 1] - left=1, right=1, total 1*1
sum= 1

- N = 4: 0,1
(1 + 3)
[1, 1, 2] - left=1, right=0
[2, 1, 1] - left=0, right=1
[0, 1, 3] - left=1, right=1 - total=1
[3, 1, 0] - left=1, right=1 - total=1
sum=2

- N = 5: 0,1,2
(1+4)
[0, 1, 4]
[4, 0, 1]
[1, 1, 3]
[3, 1, 1]
[2, 1, 2]


what to return?
    list[all possible trees]
what to do in each level?
    for i in [0, N/2]:
        leftRes=func[i]
        rightRes=func[N-i-1]

"""