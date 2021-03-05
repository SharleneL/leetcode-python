import collections
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = collections.defaultdict(int)  # <v, color> color=-1 or 1

        def dfs(v: int, parent_color: int) -> bool:
            if color[v]:
                return color[v] == -parent_color
            color[v] = -parent_color

            can_bipartite = True
            for u in graph[v]:
                can_bipartite = can_bipartite and dfs(u, -parent_color)

            return can_bipartite

        res = True
        for i in range(len(graph)):
            if not color[i]:
                res = res and dfs(i, -1)
        return res

if __name__ == '__main__':
    res = Solution().isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]])
    print(res)
