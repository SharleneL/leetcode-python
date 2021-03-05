"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    # DFS
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = collections.defaultdict(Node)

        # 这个递归函数返回的是input node的cloned node
        def dfs(node: 'Node') -> 'Node':
            if not node:
                return
            if node in visited:
                return visited[node]

            new_node = Node()
            new_node.val = node.val
            visited[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(dfs(n))

            return new_node

        return dfs(node)

    # BFS
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = collections.defaultdict(Node)
        if not node: return
        clone = Node(node.val)
        visited[node] = clone
        queue = deque()
        queue.appendleft(node)
        while queue:
            tmp = queue.pop()
            for n in tmp.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    queue.appendleft(n)
                visited[tmp].neighbors.append(visited[n])
        return clone


'''
BFS traversal:
q.add(n)
while q:
    cn = q.pop
    enq each neightbor of cn, if not visited


DFS traversal:
print node.val
for each n of node.neighbors:
    if not in visited:
        dfs(n)
'''