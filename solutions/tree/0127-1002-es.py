# 这题不简单啊。。
# 对于每个str，维护一个len=26的arr；记录当前str中每个ch出现的次数
# 同时维护一个全局的len=26的arr，用来记录每个ch出现的最小次数
# 比如：

# - "abc" cur_arr = [1,   1,   1,   0]
# -       min_arr = [MAX, MAX, MAX, MAX]
# -       上2个求min [1,   1,   1,   0]

# - "bbc" cur_arr = [0,   2,   1,   0]
# -       min_arr = [1,   1,   1,   0]
# -       上2个求min [0,   1,   1,   0]  -- a在第二个str中没有出现所以是0

# 用法：
# sys.maxsize
# ord('b') -- unicode码; e.g. ord(ch)-ord('a')
# chr(90)  -- unicode -> ch; e.g. chr(ord('a')+i
# [1, 2].extends([3]*2) -- [1, 2, 3, 3]
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        min_res = [sys.maxsize] * 26
        for s in A:
            cur_res = [0] * 26
            for ch in s:
                cur_res[ord(ch) - ord('a')] += 1
            for i in range(26):
                min_res[i] = min(min_res[i], cur_res[i])

        res = []
        for i in range(26):
            if min_res[i] != sys.maxsize:
                res.extend([chr(ord('a') + i)] * min_res[i])

        return res