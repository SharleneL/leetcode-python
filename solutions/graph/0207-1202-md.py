# https://leetcode-cn.com/problems/smallest-string-with-swaps/solution/python3-bing-cha-ji-ha-xi-biao-pai-xu-ji-pxay/
# 要扫三遍！记住unionfind中parent的value是下标不是值！
# 总结：如何在unionfind中用dict来解题 得到每个cluster中item的下标及value：
# 1. 先将所有edge union起来
# 2. 定义dict成<rootIndex, list[itemIndex]>, 对每个item找root然后加入dict
# 3. 取出每一个list[itemIndex]即得到每个cluster的所有item的下标，在str中即可找到相应item。此时我们得到了该cluster中item的下标&&item的值。因此可以进行任何操作了。
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 第一遍：将所有edge过一遍，将所有下标union起来 （注意：是index！）
        n = len(s)
        uf = UnionFind(n)
        for x, y in pairs:
            uf.union(x, y)

        # 第二遍：
        # 遍历str中的每个ch的index；找到其root的index
        # 用一个dict来记录<root_ch_index, list[ch_index]> - 其中value的值为相同root的ch的index
        from collections import defaultdict
        dic = collections.defaultdict(list)
        for i in range(n):
            ch_root_idx = uf.find(i)
            dic[ch_root_idx].append(i)

        # 第三遍：遍历dict中的k, v；注意v是list[index_of_ch_in_str]
        # 找到v中每个index所对应的str中的ch，并按照字典排序，得到一个ch_arr
        # 同时遍历v和ch_arr，此时注意:
        #    从前到后遍历v，得到的是该cluster中所有ch的index，并且是从小到大排列的
        #    从前到后遍历ch_arr，得到的是该cluster中所有ch按照字典排序的ch值
        # 因此在遍历的过程中可以将result list中下标为v[i]的item赋值为ch_arr[i]
        res = ["_"] * n
        for ch_root, indices in dic.items():
            ch_arr = list()
            for i in indices:
                ch_arr.append(s[i])
            ch_arr.sort()
            for i in indices:
                res[i] = ch_arr.pop(0)

        return ''.join(res)

    # UnionFind模板 完全没有变化


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
        self.size[x] += self.size[y]