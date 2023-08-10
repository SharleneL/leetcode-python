import heapq


class MyPriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    # if `priority` is smaller, the item is ranked higher.
    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        val = heapq.heappop(self._queue)[-1]
        return val

    def is_empty(self):
        return len(self._queue) == 0


class Solution:
    # 需要定义在class level，这样每次call topKFreq()都可以access到同一个obj
    pq = MyPriorityQueue() # top is the min
    out_q_map = {}

    # push n into heap, allowed max heap size is k
    # heap's top is the val with largest freq
    def topKFrequent(self, n, k):
        if n in Solution.out_q_map:
            freq = Solution.out_q_map[n] + 1
            pair = (n, freq)
            self.pq.push(pair, -freq) # largest freq should go to the top. `priority` is smaller the item is ranked higher.
        else:
            self.pq.push(-1, (n, 1))

        if len(self.pq._queue) > k:
            min_freq_pair = self.pq.pop()
            self.out_q_map[min_freq_pair[0]] = min_freq_pair[1]

        # print res
        print(Solution().pq)
        print(Solution().out_q_map)



    def test(self):
        k = 2
        self.topKFrequent(1, k)
        self.topKFrequent(1, k)
        self.topKFrequent(2, k)
        self.topKFrequent(3, k)
        self.topKFrequent(2, k)

# test
if __name__ == '__main__':
    Solution().test()
