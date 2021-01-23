class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        # 先得到如果没有zigzag的情况下的path（即每层都是从左到右排列）
        while label != 0:
            res.append(label)
            label = int(label / 2)  # need to convert to int!!!

        level_size = len(res)
        i = 1
        while i < level_size:
            cur_level = level_size - i
            # 如果zigzag反过来的话，那么隔一层需要flip一下数字
            # 怎么flip呢？每一层左右两个数字相加的和都是
            # 2^()n-1 + 2^n - 1
            res[i] = pow(2, cur_level - 1) + pow(2, cur_level) - 1 - res[i]
            i += 2

        # 因为我们最开始是从下往上得到的无zigzag path，所以返回之前要reverse一下
        res.reverse()
        return res

