import queue
from typing import List, Dict, Tuple

"""
- 0: emptyLand
- 1: building
- 2: obstacle

- Target: for all emptyLand in the matrix, find the one with the `shortestTotalDist` to all buildings.
- 我们可以从building出发，for each building: 用dfs或者bfs来fill in所有emptyLand到这个building的dist, 然后加总，最后找最小
- 因为matrix里本来就存着非零整数，直接update matrix并不理想。
    方法一：用多个matrix来存dist。每个building都create一个matrix。
        但是这个matrix里面只需要存emptyLand的值，其他space（比如对应building和obstacle的位置）都被浪费了
    方法二：用map来存dist。可以用一个map来存当前building的dist，另一个存总的。
        for each building: distMap[(i, j)] = val  # saves the shortest dist bw current building & emptyLand [i, j]
        每个buildling iterate完之后，用map里面的值加总到总map里。
"""


class Solution:
    def shortestDistance(self, grid:List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        # TODO edge case: row=1 & col=1
        if row<1:
            return 0

        total_shortest_dist_map = {}
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1: # for each building, do BFS or DFS, get a map: shortest dist from this building to ALL emptyLands
                    shortest_dist_from_bldg_map = self.getShortestDistMapForBldg(i, j, grid)

                    # add shortest_dist_from_bldg_map into total_shortest_dist_map
                    for key in shortest_dist_from_bldg_map.keys():
                        a, b = key
                        if (a, b) in total_shortest_dist_map:
                            total_shortest_dist_map[(a, b)] += shortest_dist_from_bldg_map[(a, b)]
                        else:
                            total_shortest_dist_map[(a, b)] = shortest_dist_from_bldg_map[(a, b)]

        # pick the shortest val from total_shortest_dist_map
        vals = total_shortest_dist_map.values()
        minVal = min(vals)
        return minVal

    # return shortest dist from input building to ALL emptyLands
    # return value: a map
    # key: an int pair, coordinates of empty land
    # val: int, shortest dist from bldg (a, b)
    def getShortestDistMapForBldg(self, bldg_i, bldg_j, grid) -> Dict[Tuple[int, int], int]:
        shortest_dist_from_bldg_map = {}
        m = len(grid)
        n = len(grid[0])

        # start from bldg_i, bldg_j, update all connected emptyLands
        # bfs:
        q = queue.Queue()
        q.put((bldg_i, bldg_j))
        shortest_dist_from_bldg_map[(bldg_i, bldg_j)] = 0
        while not q.empty():
            (i, j) = q.get()
            last_step_dist = shortest_dist_from_bldg_map[(i, j)]
            # process up/down/left/right
            self.dfsProcessor(i - 1, j, grid, m, n, shortest_dist_from_bldg_map, last_step_dist, q)
            self.dfsProcessor(i + 1, j, grid, m, n, shortest_dist_from_bldg_map, last_step_dist, q)
            self.dfsProcessor(i, j - 1, grid, m, n, shortest_dist_from_bldg_map, last_step_dist, q)
            self.dfsProcessor(i, j + 1, grid, m, n, shortest_dist_from_bldg_map, last_step_dist, q)

        # remember to remove the bldg
        shortest_dist_from_bldg_map.pop((bldg_i, bldg_j))
        return shortest_dist_from_bldg_map

    def dfsProcessor(self, i, j, grid, m, n, shortest_dist_from_bldg_map, last_step_dist, q):
        # if out of bound: return
        if i<0 or i>=m or j<0 or j>=n:
            return
        # if is bldg or obstacle: return
        if grid[i][j] == 1 or grid[i][j] == 2:
            return

        # if is emptyLand:
        # if NOT in map: add to map, dist=min(map_val, map's dist_val+1)
        if (i, j) not in shortest_dist_from_bldg_map:
            shortest_dist_from_bldg_map[(i, j)] = last_step_dist + 1
            q.put((i, j))
        # if is in map: update val to min(map_val, map's dist_val+1)
        else:
            cur_dist = shortest_dist_from_bldg_map[(i, j)]
            if cur_dist > last_step_dist + 1:
                shortest_dist_from_bldg_map[(i, j)] = last_step_dist + 1
                q.put((i, j))



# test
if __name__ == '__main__':
    A = [
        [1,0,2,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0]
    ]
    res = Solution().shortestDistance(A)
    print(res)
