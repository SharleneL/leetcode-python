# 只要找到入度为0的所有点即可。因为入度>0表示总有别的点可以到达该点

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []  # indegree==0's set
        in_degree = [0] * n
        for edge in edges:
            in_degree[edge[1]] += 1

        print(in_degree)
        for i in range(n):
            if in_degree[i] == 0:
                res.append(i)

        return res


'''
input:
- edges[i] = [a, b] a->b; i: vertices number

output:
- min set of i; i cann reach all graph
'''