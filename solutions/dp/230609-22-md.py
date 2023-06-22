# TODO：过了。但是时间复杂度？空间复杂度？
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return list(self.helper(n))

    def helper(self, n) -> Set[str]:
        if n == 1:
            return set(["()"])

        totalSet = set()
        for pCombinationStr in self.helper(n - 1):
            newResSet = set()
            for i in range(len(pCombinationStr) - 1):
                if pCombinationStr[i] == '(':
                    newResSet.add(pCombinationStr[:i] + "()" + pCombinationStr[i:])
                    newResSet.add(pCombinationStr[:(i + 1)] + "()" + pCombinationStr[(i + 1):])
            newResSet.add(pCombinationStr + "()")
            totalSet |= newResSet

        return totalSet


"""
1: ()
2: ()() ; (())
3: ()()() ; (())() : ()(())
   ()(()) ; (()()) ; ((())) ; (()()) ; (())()

不断插入，碰到"("的话，在(之前或者之后都可以插入一对括号。
会有重复值，因此用set来存储。

# gen all () combinations for n
helper(n)

# if I know the value of helper(n-1):
totalSet = ()
for each pCombinationStr in helper(n-1):
    newResSet = ()
    for each ch, idx in pCombinationStr:
        if ch == '(':
            newResSet.add(
                pCombinationStr[:idx] + "()" + ch + pCombinationStr[idx:],
                pCombinationStr[:idx] + ch + "()" + pCombinationStr[idx:],
            )
    newResSet.add(pCombinationStr+"()")
totalSet.addAll(newResSet)
return totalSet

# starting value
if n == 1: return "()"
"""