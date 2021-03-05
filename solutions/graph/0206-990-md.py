from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # first round: union all the == nodes
        uf = UnionFind(26)
        for str in equations:
            if str[1] == '!':
                continue
            # process == pairs
            x = ord(str[0]) - ord('a')
            y = ord(str[-1]) - ord('a')
            uf.union(x, y)

        # second round: check all the != pairs - if any of those 2 are connected, then return false
        for str in equations:
            if str[1] == '=':
                continue
            # process != pairs
            x = ord(str[0]) - ord('a')
            y = ord(str[-1]) - ord('a')
            if uf.isConnected(x, y):
                return False
        return True


class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parents[y] = x
        self.size[x] = self.size[x] + self.size[y]

    def isConnected(self, x: int, y: int):
        x = self.find(x)
        y = self.find(y)
        return x == y


if __name__ == '__main__':
    res = Solution().equationsPossible(["a==b", "b!=a"])
    print(res)