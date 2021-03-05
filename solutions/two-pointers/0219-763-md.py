'''
没思路的时候，记得要找例子、画图！
用人脑想一下该怎么解决这个问题，然后再interpret成程序

这个问题，比如序列是abcaecbd
先看a，找到a所在的最后出现的index是3，那么第一个subset最少也要涵盖到3
再看0-3之间的char，b最后出现位置是6，则extend tail pointer到6
至此我们知道可以用2pointer来解
所以我们用head来keep住当前序列的最开始的地方，然后用一个i来遍历head和tail之间的元素，不断extend tail的值。当i == tail的时候，证明找到了一个set
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = collections.defaultdict(list)
        for i in range(len(S)):
            ch = S[i]
            dic[ch].append(i)

        res = list()

        head = 0
        tail = 0
        i = head
        while i < len(S):
            ch = S[i]
            ch_last_idx = max(dic[ch])
            tail = max(tail, ch_last_idx)
            if i == tail:
                res.append(tail - head + 1)
                head = tail + 1
                tail = tail + 1

            i += 1

        return res

