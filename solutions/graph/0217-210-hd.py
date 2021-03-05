import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # prep adj
        adj = collections.defaultdict(list)
        total_word_cnt = len(wordList)

        for i in range(total_word_cnt):
            w1 = beginWord
            w2 = wordList[i]
            dist = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    dist += 1
                    if dist > 1:
                        continue
                if dist == 1:
                    adj[w1].append(w2)
                    adj[w2].append(w1)

        for i in range(total_word_cnt):
            for j in range(i + 1, total_word_cnt):
                w1 = wordList[i]
                w2 = wordList[j]
                dist = 0
                for i in range(len(w1)):
                    if w1[i] != w2[i]:
                        dist += 1
                        if dist > 1:
                            continue
                if dist == 1:
                    adj[w1].append(w2)
                    adj[w2].append(w1)

        print(adj)
        # BFS
        level_cnt = 1
        visited = set()
        q = collections.deque()
        q.append(beginWord)
        cur_level_size = len(q)
        while q:
            # process popped elem
            cur = q.popleft()
            visited.add(cur)
            if len(visited) == len(wordList) + 1:
                return 0

            # process children
            for child in adj[cur]:
                if child in visited:
                    continue
                if child == endWord:
                    return level_cnt + 1
                q.append(child)

            # process level
            cur_level_size -= 1
            if cur_level_size == 0:
                level_cnt += 1
                cur_level_size = len(q)

        return 0


if __name__ == '__main__':
    res = Solution().ladderLength("leet", "code", ["lest","leet","lose","code","lode","robe","lost"])
    print(res)

'''
adj list:
[hit] -> hot, x, x
[hot] -> dot, x, x
[dot] -> dog, x, x

start = hit
end = cog

# BFS
level = 0
visited = set
queue = Q

enqueue(start)
cur_level_size = q.size
while q:
    cur = q.pop
    if cur in visited: return False # there is circle
    visited.add(cur)
    cur_level_size--
    if cur_level_size == 0: level++
    for next in adj[cur]:
        if next == end: return level
        else: enqueue(next)

return level
'''