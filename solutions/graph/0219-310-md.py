class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        min_dict = collections.defaultdict(int)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        print(adj)

        def get_longest_path(n: int, last_parent: int, adj) -> int:
            nonlocal min_dict
            if not adj[n]:
                return 0
            if min_dict[n]:
                return min_dict[n]
            longest_path = 0
            for v in adj[n]:
                if v is not last_parent:
                    longest_path = max(longest_path, get_longest_path(v, n, adj))
            min_dict[n] = longest_path + 1
            return longest_path + 1

        res = list()
        min_height = sys.maxsize
        for i in range(n):
            cur_min_height = get_longest_path(i, -1, adj)
            print(i)
            print(cur_min_height)
            if cur_min_height == min_height:
                res.append(i)
            elif cur_min_height < min_height:
                res = [i]
                min_height = cur_min_height

        return res


'''
connected G no sycle

input:
- n - nodes
- edges[i]=[a, b] - a<>b

拎起来
output:
- all possible min height t's roots

height: # edges


think:
- must traverse all nodes & find the height if use that node as the root
- for each node: cal the longest path

n = 4, nodes = [0 1 2 3]
minH = MAX
for i in range(4):
    cur_longest = find longest route starting from i # TODO
    minH = min(minH, cur_longest)

return minH
'''