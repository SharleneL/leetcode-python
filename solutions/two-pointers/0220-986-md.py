'''
解法：每次从A中拿一个interval，从B中拿一个interval。得到这一对interval的intersection
我开始一直没有从interval的granularity来想，而是从更小的单个数字的level去想。所以一直想的是用两个pointer指来指去
最后的解法是每次挑两个interval出来求交集
相当于是首先用two pointer来指向两个interval
然后在求一对interval内部的交集
'''
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        len1 = len(firstList)
        len2 = len(secondList)
        idx1 = 0  # index of current interval
        idx2 = 0
        res = list()

        while idx1 < len1 and idx2 < len2:
            interval1 = firstList[idx1]
            interval2 = secondList[idx2]

            # find intersection of current 2 intervals
            ah, at = interval1[0], interval1[-1]
            bh, bt = interval2[0], interval2[-1]
            print(str(ah) + ' ' + str(at))
            print(str(bh) + ' ' + str(bt))
            if bt < ah:
                idx2 += 1
                continue
            elif bh > at:
                idx1 += 1
                continue
            else:
                intersection_h = max(bh, ah)
                intersection_t = min(at, bt)
                res.append([intersection_h, intersection_t])
                if at <= bt: # 往后挪指针的地方很容易错。搞不清楚的时候就挑两个例子写一写伪代码
                    idx1 += 1
                if bt <= at:
                    idx2 += 1
        return res


'''
input:
- firstList
- secondList

output: 
intersection of 2 interval lists

def:
- closed interval: 
- intersection: included in both intervals


每次从A中拿一个interval，从B中拿一个interval。得到这一对interval的intersection
需要的有：ah, at; bh, bt (当前interval的head和tail)
if bt<ah or bh>at:
    no intersection
    if bt<ah:
        b ++
    else:
        a ++
else:
    intersection_h = min(bh, ah)
    intersection_t = min(at, bt)
    add intersection to res
    a ++
    b ++
'''