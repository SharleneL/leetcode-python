class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for s in stones:
            if s in jewels:
                cnt += 1

        return cnt


"""
input:
- str j: types of stones
- str s: stones I have; each char is a type of stone I have

output:
- # of I have stones are jewels

for each ch in stones:
    if in jewels:
        cnt++
"""