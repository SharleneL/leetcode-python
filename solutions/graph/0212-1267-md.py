class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_cnt = [0] * len(grid)
        col_cnt = [0] * len(grid[0])

        for i in range(len(row_cnt)):
            for j in range(len(col_cnt)):
                if grid[i][j] == 1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1

        res = 0
        for i in range(len(row_cnt)):
            for j in range(len(col_cnt)):
                if grid[i][j] == 1 and (row_cnt[i] > 1 or col_cnt[j] > 1):
                    res += 1

        return res


'''
input: 
- grid
[
[1,1,0,0],
[0,0,1,0],
[0,0,1,0],
[0,0,0,1]
]

output
- # of Non-isolated server

解法：
- iterate each row: count # servers in this row. 
- iterate each col: count # servers in this col
- iterate each [i][j] in matrix, check row_cnt[] and col_cnt[], if any>=2 then count into total
'''