class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # get reverse adj grapj: [i, [a, b]] a->i, b->i
        adj = collections.defaultdict(list)
        total_count = len(graph)
        indegree = [0] * total_count
        for cur_node in range(total_count):
            for next_node in graph[cur_node]:
                adj[next_node].append(cur_node)
                indegree[next_node] += 1

        visited = 0
        q = deque()
        res = list()
        for cur_node in range(total_count):
            if indegree[cur_node] == 0:
                q.append(cur_node)
        while q:
            cur_node = q.popleft()
            res.append(cur_node)
            for in_node in adj[cur_node]:
                indegree[in_node] -= 1
                if indegree[in_node] == 0:
                    q.append(in_node)

        return res


'''
remove all nodes which are in a circle
- reverse adj graph + indegree[i]
- all nodes with outdegree==0: 
    all in node of this node, outdegree--
    till all are visited
'''