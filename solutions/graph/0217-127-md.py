# BFS
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         res = list()
#         edges = collections.defaultdict(list)
#         indegree = [0] * numCourses

#         for u, v in prerequisites:
#             edges[v].append(u)
#             indegree[u] += 1

#         queue = collections.deque()
#         for i in range(numCourses):
#             if indegree[i] == 0:
#                 queue.append(i)

#         while queue:
#             cur_node = queue.popleft()
#             res.append(cur_node)
#             for next_node in edges[cur_node]:
#                 indegree[next_node] -= 1
#                 if indegree[next_node] == 0:
#                     queue.append(next_node)

#         if len(res) == numCourses:
#             return res
#         else:
#             return []


# '''
# BFS:

# edges = dict()
# for u, v in preq: # v -> u
#     edges[v].append(u)
#     indegree[v]++ # TODO def
#     enqueue indegree==0 # TODO def

# while q:
#     popleft
#     indegree[next]--
#     if ==0: enqueue

# visited == totalNum # TODO def
# '''


# DFS
# 注意1.变成2之后再append到list 2.要reverse了之后再返回
# DFS其实是一探到底，得到最难的course，加到list里面，然后再返回上一层
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(n: int) -> bool:  # return if n and its subnodes has circle
            if color[n] == 2:  # TODO def
                return False
            if color[n] == 1:
                return True

            color[n] = 1
            for v in edges[n]:  # TODO def
                has_circle = dfs(v)
                if has_circle:
                    return True
            # no circle in subnodes
            color[n] = 2
            res.append(n)  # TODO def
            return False

        color = [0] * numCourses
        res = list()
        edges = collections.defaultdict(list)
        for a, b in prerequisites:
            edges[b].append(a)

        for i in range(numCourses):
            has_circle = dfs(i)
            if has_circle:
                return []

        res.reverse()
        return res


'''
DFS: color
for each node:
    dfs(n): # return if cur node's subnodes has circle & append to res
    if not dfs(n) return []
    else return res

def dfs(n):
    if color[n] == 1: return True # TODO def
    if color[n] == 2: return False
    color[n] = 1
    res.append(n)
    cur_res = False
    for each next nodes:
        res = dfs(n)
        if res: return True
    color[n] = 2
    return False
'''