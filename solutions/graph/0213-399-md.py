'''
解法：https://leetcode-cn.com/problems/evaluate-division/solution/399-chu-fa-qiu-zhi-nan-du-zhong-deng-286-w45d/
1.定义UnionFind(n): 要对元素编号
2.要对每一对edge做union; union的过程使用find; find的时候路径压缩+update weights
3. 最后一步查询结果：调用isConnected

- 分析题意，其实可以把数字之间的关系表示成一个有权有向图
- 可以通过并查集来实现：如果两个var是connected，则通过union他们的过程来找到这两个点之间的权值（union的时候需要用到find，在find的时候路径压缩，直到A点和B点相连）

如何实现？
1.如何表示UnionFind？UF中往往用单个index来代表一个值，所以我们需要用一个HashMap来将index和var给map起来。所以Map的key是index，value是var的名字。
'''


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 预处理：（UnionFind第一步：编号）
        # equations是边；equations的两端是nodes；我们需要给所有node来编号——因为UnionFind中需要用编号来找到某个node
        # 用一个map来维护编号和node之间的关系：node -> index
        idx = 0
        varToIdx = dict()
        uf = UnionFind(len(equations) * 2)  # 因为我们最差情况是equations中所有pair都互不相同
        for i in range(len(equations)):
            a, b = equations[i]
            # 编号
            if not a in varToIdx:
                varToIdx[a] = idx
                idx += 1
            if not b in varToIdx:
                varToIdx[b] = idx
                idx += 1

            # 将每一条边两个node的index加入uf中，从而uf中有了所有connection的info
            uf.union(varToIdx[a], varToIdx[b], values[i])

        # 接下来：处理
        # 用uf的isConnected来查询两个node是否在同一个set中 && if yes则计算他们到其parent的weight来得到这两者之间的weight
        res = [0.0] * len(queries)
        for i in range(len(queries)):
            a, b = queries[i]

            if a not in varToIdx or b not in varToIdx:
                res[i] = -1.0
                continue

            idx_a = varToIdx[a]
            idx_b = varToIdx[b]
            if not idx_a or not idx_b:
                res[i] = -1.0
            else:
                res[i] = uf.isConnected(idx_a, idx_b)

        return res


class UnionFind:
    def __init__(self, n: int):
        # 起始状态：每个node的parent是自己；所以每个node到parent的weight都是1
        self.parents = list(range(n))
        self.weights = [1.0] * n  # 记录当前node除以其所在tree的parent的value

    # isConnected来查询+计算a, b两个index所表示的node之间的weight：
    # 如果两个node不在同一个set中，返回-1
    # 如果在同一个set中，则node_a/parent=weight[a], node_b/parent=weight[b] => 则 node_a/node_b = weight[a]/weight[b]
    def isConnected(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            return -1.0
        return self.weights[a] / self.weights[b]

    # union做了什么事？
    # input：a与b这两个index表示的node之间相连，并且node_a/node_b = value
    # output: 找a的root，找b的root，将root_a的parent设成root_b（不用比较两个cluster的size是因为我们在find的时候用了压缩路径，每个node的parent都是整个tree的parent），并update weights[a]
    def union(self, a: int, b: int, value: float):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return  # no need to reassign parents or update weights

        self.parents[root_a] = root_b
        # 因为：
        # a到root_a的权值为weights[a]: var_a/var_root_a = weights[a]
        # b到root_b的权值为weights[b]: var_b/var_root_b = weights[b]
        # var_a / var_b = value
        # 所以 var_root_a / var_root_b = (w[b]/w[a])*value
        self.weights[root_a] = self.weights[b] * value / self.weights[a]

    # input: 某个node的idx
    # output：将var_x这个node append到能找到的root上，并update weights[x]成为var_x/root_x的值
    def find(self, x: int):
        if x == self.parents[x]:
            return x
        origin_parent = self.parents[x]
        self.parents[x] = self.find(self.parents)
        self.weights[x] *= self.weights[origin_parent]
        return self.parents[x]


'''
input:
- equations[i][j]
    e[i] = [A, B]
- values[i]
    v[i] = A / B
- queries[i][j]
    q[i] = [C, D]

output:
    C/D
'''