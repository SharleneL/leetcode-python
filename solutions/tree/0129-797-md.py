'''
1.termination有两种：到达N-1或者达到尽头。只有第一种情况需要加到res里面。
2.返回之前path需要pop；加入res的时候需要copy
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.dfs(graph, res, [], 0)
        return res

    def dfs(self, graph: List[List[int]], res: List[List[int]], cur_path: List[int], cur_node: int):
        cur_path.append(cur_node)
        if cur_node == len(graph) - 1:
            res.append(cur_path.copy()) # 加入res的时候需要copy
            cur_path.pop() # 返回之前path需要pop
            return
        elif not graph[cur_node]:
            cur_path.pop() # 返回之前path需要pop
            return
        else:
            for node in graph[cur_node]:
                self.dfs(graph, res, cur_path, node)
            cur_path.pop() # 返回之前path需要pop


'''
input:
- graph: graph[i]=[a, b, c] -> i can reach a/b/c

res = [] # paths

- what to return to last level? 
- what to do? 
    for each elem in graph[i]
'''