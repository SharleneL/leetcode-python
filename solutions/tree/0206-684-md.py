'''
给edge寻找导致成环的edge; 一个个遍历edge，如果两个node的root不同则union起来，如果node的root相同则当前edge就是导致成环的edge

- 如果两个顶点属于不同的set(root不同)，则说明在遍历到当前的边之前，这两个顶点之间不连通，因此当前的边不会导致环出现，合并这两个顶点的连通分量。
- 如果两个顶点属于相同的set，则说明在遍历到当前的边之前，这两个顶点之间已经连通，因此当前的边导致环出现，为附加的边，将当前的边作为答案返回。
'''


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for x, y in edges:
            if uf.find(x) != uf.find(y):
                uf.union(x, y)
            else:
                return [x, y]
        return []


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n + 1))  # 需要+1，因为node的val是从1开始的
        self.size = [1] * (n + 1)

    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        x = self.find(self.parents[x])
        y = self.find(self.parents[y])
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parents[y] = x
        self.size[x] += self.size[y]

    def isConnected(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        return x == y


'''
definition:
- tree, undirected, no cycle

input:
- graph: as a tree, N nodes diff vals [1-N] + 1 additional edge
    edge: 2 diff vals && is 节外生枝

output:
- 2D arr of edges: List[edges] && edge=[u, v]: u<v (uv are connected)

return the 节外生枝的edge
'''