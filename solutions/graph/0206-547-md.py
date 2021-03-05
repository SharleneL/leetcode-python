class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # create union find
        # for each connection in isConnected, call uf.union
        # return uf.setCount
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
        return uf.setCount


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.setCount = n
        self.n = n

    # find root of x
    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.setCount -= 1
        self.size[x] = self.size[x] + self.size[
            y]  # no need to update size[y] as y is not the root anymore and will not be found in the future
        return