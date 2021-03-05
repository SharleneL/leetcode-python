class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # create union find
        # for each connection in isConnected, call uf.union
        # return uf.setCount
        if len(connections) < n - 1:
            return -1

        uf = UnionFind(n)
        for x, y in connections:
            uf.union(x, y)
        return uf.setCount - 1


# TEMPLATE FOR UNION FIND
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n  # used in union; log how many nodes in a node's set. union small one to large one.
        self.n = n

        self.setCount = n  # how many disconnected sets are there

    # find root of a node
    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(
            self.parent[x])  # this also set each node in the path's parent as the root!! good good
        return self.parent[x]

    # connect any node x & y's roots
    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:  # append small set to big set. make sure x is the larger
            x, y = y, x
        self.parent[y] = x  # y's parent is x
        self.size[x] += self.size[
            y]  # no need to update size[y] as y is not the root anymore and will not be found in the future
        self.setCount -= 1
        return True

    # check if x y are connected
    def isConnected(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        return x == y


'''
union find to find the # of unconnected clusters
#-1 is the answer 
'''