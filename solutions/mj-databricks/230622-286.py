from typing import List
import queue

""" Matrix相关的BFS和DFS。
if is 2147483647: emptyRoom.
if is -1: wall
if is 0: gate

for each emptyRoom in matrix:
    dist to it's nearest 0
    
===== thoughts =====
for each gate, update all nearby emptyRooms. BFS

for each emptyRoom, recursively find it's path
def minGateDist(i, j): # for emptyRoom located in (i, j), shortest dist to any gate
    # edge cases TODO
    # if i<1 || j<1 || i<=len(rooms)-1 || j<=len(rooms)-1
    if i<0 or j<0 or i>=len(rooms) or j>=len(rooms): # aka is out of boundary
        return INF
    
    # i>=0 && i<len(rooms); j>=0 && j<len(rooms)
    if rooms[i][j] is Wall: return INF
    if rooms[i][j] is Gate: return 0
    if rooms[i][j] is EmptyRoom:
        return min(
            minGateDist(i-1, j),
            minGateDist(i+1, j),
            minGateDist(i, j-1),
            minGateDist(i, j+1)
        ) + 1
        
    we only need to DFS each 封闭 emptyRoom. use first path to find all isolatedEmptyRooms.
    or, find any emptyRoom, do dsf, then continue, till all grids in the matrix are filled out
"""


"""
bfs解法：
1: iterate matrix, push all gate into queue
2:
 - pop 1 room from queue
    for 上下左右 of the room:
        if出界: do nothing
        if is INF: = roomVal+1; enqueue
        if is 0 or -1: do nothing
        else:
            if 上下左右's curVal > roomVal+1:
                上下左右's curVal = roomVal +1
                并且enqueue
            else: do nothing
"""
# class Solution:
#     def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
#         if len(rooms) < 1:
#             return rooms
#
#         q = queue.Queue()
#         m = len(rooms)
#         n = len(rooms[0])
#         for i in range(m):
#             for j in range(n):
#                 if rooms[i][j] == 0:
#                     q.put((i, j))
#
#         while not q.empty():
#             (i, j) = q.get()
#             # up
#             self.dfsProcessor(q, rooms, m, n, i, j, i - 1, j)
#             # down
#             self.dfsProcessor(q, rooms, m, n, i, j, i + 1, j)
#             # left
#             self.dfsProcessor(q, rooms, m, n, i, j, i, j - 1)
#             # right
#             self.dfsProcessor(q, rooms, m, n, i, j, i, j + 1)
#
#         return rooms
#
#
#     def dfsProcessor(self, q, rooms, m, n, cur_i, cur_j, next_i, next_j):
#         if next_i<0 or next_i>=m or next_j<0 or next_j>=n:
#             return
#         if rooms[next_i][next_j] == 0 or rooms[next_i][next_j] == -1:
#             return
#         elif rooms[next_i][next_j] == 2147483647:
#             rooms[next_i][next_j] = rooms[cur_i][cur_j] + 1
#             q.put((next_i, next_j))
#             return
#         elif rooms[next_i][next_j] > rooms[cur_i][cur_j] + 1:
#             rooms[next_i][next_j] = rooms[cur_i][cur_j] + 1
#             q.put((next_i, next_j))
#             return

"""
dfs
for each gate: dfs update connected room
dfs(i, j, last_dist, rooms):
    if (i, j) out of bound: return
    if (i, j) = -1: return
    if (i, j) = 0: return
    if (i, j) = INF: rooms[i][j] = last_dist+1
    else: if (i, j) > rooms[i][j] = last_dist+1: rooms[i][j] = last_dist+1  
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        m = len(rooms)  # total rows
        n = len(rooms[0])   # total cols
        if m == 0:
            return rooms

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:    # is gate
                    self.dfs(i-1, j, m, n, rooms, 0)
                    self.dfs(i+1, j, m, n, rooms, 0)
                    self.dfs(i, j-1, m, n, rooms, 0)
                    self.dfs(i, j+1, m, n, rooms, 0)

        return rooms

    def dfs(self, i, j, m, n, rooms, last_dist):
        # process current layer
        if i<0 or i>=m or j<0 or j>=n:
            return
        if rooms[i][j] == 0 or rooms[i][j] == -1:
            return

        if rooms[i][j] > last_dist+1:
            rooms[i][j] = last_dist+1
            # only need to proceed to next layer if cur layer is updated
            self.dfs(i - 1, j, m, n, rooms, last_dist+1)
            self.dfs(i + 1, j, m, n, rooms, last_dist+1)
            self.dfs(i, j - 1, m, n, rooms, last_dist+1)
            self.dfs(i, j + 1, m, n, rooms, last_dist+1)

        # test
if __name__ == '__main__':
    M = [
        [2147483647,-1,         0,          2147483647],
        [2147483647,2147483647, 2147483647, -1],
        [2147483647,-1,         2147483647, -1],
        [0,         -1,         2147483647, 2147483647]
    ]

    res = Solution().wallsAndGates(M)
    print(res)
