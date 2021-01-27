class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if not arr:
            return False

        val_to_occ = dict()
        for val in arr:
            if val not in val_to_occ:
                val_to_occ[val] = 1
            else:
                val_to_occ[val] += 1
        occ_list = set(val_to_occ.values())
        return len(occ_list) == len(val_to_occ)


"""
input:
- arr[int]

output:
- T if+only if #occ is uniq
"""