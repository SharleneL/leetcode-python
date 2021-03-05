# DFS
class Solution:
    visited = set()

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = set()  # 注意！！class变量一定要重新赋值一遍！不然里面的value会被保存到下一次submit！
        self.dfs(0, rooms)
        return len(self.visited) == len(rooms)

    def dfs(self, cur_room_idx: int, rooms: List[List[int]]):
        self.visited.add(cur_room_idx)
        next_room_indices = rooms[cur_room_idx]
        for next_room_idx in next_room_indices:
            if next_room_idx not in self.visited:
                self.dfs(next_room_idx, rooms)


# BFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque
        q = deque()
        visited = set()
        q.append(0)
        visited.add(0)

        while q:
            next_room_indices = rooms[q.popleft()]
            for next_room_idx in next_room_indices:
                if next_room_idx not in visited:
                    q.append(next_room_idx)
                    visited.add(next_room_idx)

        return len(visited) == len(rooms)


'''
============================
读题目：
============================
input:
rooms[i][j]
i: [0, N-1]

N rooms[]:
- start from room[0]
- each room has distinct #: [0, N-1]
- each room MAY have same keys to access next room - ?

- room i has list of keys: rooms[i]; 
- rooms[i][j] = v: 
        v in [0-N-1]: ? opens ? with number v

- init: all rooms locked ?

output:
if you can enter every room

============================
随便取一个input然后想一下思路：
============================
rooms = [
  [1, 2],    # room0, keys=[1, 2], can go to room1 or room2
  [0, 2],    # room1, can go to room0 or room2
  [0]
]

SO:
we need to know if all rooms are connected
treat room as node
treat rooms[i] as edges from room-i to all next available rooms

============================
可能的解法：
============================
#1: unionfind:
----------------------------
- n rooms [0-n-1]
- union all rooms[i][j]
- if there's only 1 setCount then return True. all nodes are connected
BUT - this graph is directed. so we cannot use union find...

----------------------------
# 2: BFS
----------------------------
for r in rooms:


'''