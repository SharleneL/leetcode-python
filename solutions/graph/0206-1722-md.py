# 和1202是同个套路，UnionFind + HashMap得到cluster val的三部曲：

# 总结：如何在unionfind中用dict来解题 得到每个cluster中item的下标及value：
# 1. 先将所有edge中的pair通过uf.union，连起来。此时得到了index之间的tree structure【注意是index之间的！！！】
# 2. 定义一个dict，是<rootIndex, list[itemIndex]>；遍历source arr中的每个item的index；用uf.find()找到该item index的root index，然后将item index加入dict
# 3. 取出dict的values。每一个val是list[itemIndex]，即得到每个cluster的所有item的下标。接下来在str中通过index来找到相应item的val。此时我们得到了该cluster中item的下标&&item的值。因此可以进行任何操作了。

from typing import List

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        uf = UnionFind(n)
        for x, y in allowedSwaps:
            uf.union(x, y)

        from collections import defaultdict
        dic = defaultdict(list)
        for idx in range(n):
            root_idx = uf.find(idx)
            dic[root_idx].append(idx)

        dist = 0
        for root_idx, child_indices in dic.items():
            source_vals = [source[i] for i in child_indices]
            target_vals = [target[i] for i in child_indices]
            # calc the diff between source_vals and target_vals
            for v in source_vals:
                if v in target_vals:
                    target_idx = target_vals.index(v)
                    target_vals.pop(target_idx)
                else:
                    dist += 1
            dist += len(target_vals)
        return dist


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
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parents[y] = x
        self.size[x] += self.size[y]

    def isConnected(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        return x == y


if __name__ == '__main__':
    res = Solution().minimumHammingDistance([1,2,3,4], [2,1,4,5], [[0,1],[2,3]])
    print(res)


'''
input:
- arr: source[], len=n
- arr: target[], len=n
- arr: allowedSwaps[i] = [ai, bi]: can swap source[ai] & source[bi]. can swap any times + in any order

def:
- hamming dist of <source, target>: # of pos the elms are diff
    # of indice i: source[i] != target[i]

思路：
swappable的两个val应该被认为是在同一个set里面
所有swappable的val都应该同一个set里面，因为经过足够次数的swap这些val的组合可以是任何顺序
所以可以
step1根据source和allowedSwaps把source里面的val给cluster出来
step2如果source[i]和target[i]不一样的话，check他们是不是在同一个cluster；if not则distance ++
'''