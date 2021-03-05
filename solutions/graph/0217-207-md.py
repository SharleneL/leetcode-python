# BFS
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # prep adj list
#         edges = collections.defaultdict(list)
#         indegree = [0] * numCourses
#         for a, b in prerequisites: # b -> a
#             edges[b].append(a)
#             indegree[a] += 1

#         # set up vars
#         visited = 0
#         q = collections.deque([u for u in range(numCourses) if indegree[u]==0])
#         while q:
#             cur_course = q.popleft()
#             visited += 1
#             for next_course in edges[cur_course]:
#                 indegree[next_course] -= 1
#                 if indegree[next_course] == 0:
#                     q.append(next_course)

#         return visited == numCourses

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prep adj list
        edges = collections.defaultdict(list)
        for a, b in prerequisites:
            edges[b].append(a)

        # vars
        visited = [0] * numCourses  # 0-not detected; 1-detected not processed; 2-processed
        res = list()
        valid = True

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:  # not detected yet
                    dfs(v)
                    if not valid:  # if any of the children marks valid as False, it means no need to continue the recursion, return
                        return
                elif visited[v] == 1:  # has been detected before, means there is a graph
                    valid = False
                    return
            visited[u] = 2  # if not returned from above, means current node is processed. so mark as 2

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid


'''
input:
- numCourses
- arr: preq[i] = [0, 1] -> take 1 then 0; 0 depends on 1; 1->0

output:
can you finish all courses

think: judge if there is circle in the graph


BFS:
- put edges in adj list

- set up a q to store indeg==0 nodes to be processed
- set up a list to store indeg
- while q: pop, find out to what nodes, indeg--, visited++, go over list, find indeg==0, enqueue
'''