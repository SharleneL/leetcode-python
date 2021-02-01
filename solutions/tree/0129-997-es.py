# https://leetcode-cn.com/problems/find-the-town-judge/solution/yi-ge-shu-zu-gao-ding-tong-su-yi-dong-997-zhao-dao/
# 统计所有人的入度和出度信息，将满足出度为0，入度为 N - 1的节点输出
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_degree = [0] * (N + 1)
        out_degree = [0] * (N + 1)

        for t in trust:
            # t = [1, 2] 1 trust 2, 1's outdegree++, 2's indegree++
            out_degree[t[0]] += 1
            in_degree[t[1]] += 1

        for i in range(1, N + 1):
            if out_degree[i] == 0 and in_degree[i] == N - 1:
                return i
        return -1

