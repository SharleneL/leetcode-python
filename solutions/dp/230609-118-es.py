from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            self.helper(i+1, res)
        return res

    def helper(self, n, res) -> List[int]:
        if n == 1:
            res.append([1])
            return [1]
        elif n == 2:
            res.append([1, 1])
            return [1, 1]

        # below: n>2; prevRow len >=2
        prevRow = res[n-2]
        curRow = [1]
        for i in range(len(prevRow) - 1):
            curRow.append(prevRow[i] + prevRow[i + 1])
        curRow.append(1)

        res.append(curRow)
        return curRow

# test
if __name__ == '__main__':
    res = Solution().generate(5)
    print(res)

"""
input: int numRows
output: a list of arrays. is the first numRows in Ptri.

numRows = 1: [1]
numRows = 2: 

we need to calculate the first X rows in Ptr. use a resultArr to store each row.

func helper(n): # return a list of int. Contain the values of n-th row in Ptr.

imagine we already know the value of helper(n-1) # n>=1
how to get helper(n) from helper(n-1)?

prevRow = helper(n-1)
curRow = []
for i in range(len(prevRow) - 1): # aka prevRow's len must >=2
    curRow.add(prevRow[i] + prevRow[i+1])
return curRow

# thus edge case:
if len(prevRow) == 1:
"""

