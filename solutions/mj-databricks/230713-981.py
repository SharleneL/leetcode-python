class TimeMap:

    def __init__(self):
        self._tsMap = {}
        self._valMap = {}

    # Stores the key with the value value at the given time timestamp
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._valMap:
            self._valMap[key] = [value]
            self._tsMap[key] = [timestamp]
        else:
            self._valMap[key].append(value)
            self._tsMap[key].append(timestamp)

    # return val of key & ts
    # if no val exist for ts: return map[key]'s largest ts's val
    def get(self, key: str, timestamp: int) -> str:
        if key not in self._valMap:
            return ""
        if self._tsMap[key][0] > timestamp: # 不懂。edge case怎么加上来的
            return ""

        idx = self.findMostRecentTsIdx(self._tsMap[key], timestamp)
        return self._valMap[key][idx]

   # in ts_arr, find the elem <= ts
    def findMostRecentTsIdx(self, arr, target) -> int:
        total = len(arr)

        start = 0
        end = total # 不懂。为什么不是total - 1
        while start < end:
            mid_idx = (end + start) // 2  # floor division in Python!
            # if arr[mid_idx] == target:
            #     return mid_idx
            if arr[mid_idx] <= target:
                # find in [mid_idx, end]
                start = mid_idx + 1
            else:
                # find in [start, mid_idx-1]
                # end = mid_idx - 1
                end = mid_idx
        return start - 1 # 不懂。为什么要-1


# test
if __name__ == '__main__':
    timemap = TimeMap()

    timemap.set("love", "high", 10)
    timemap.set("love", "low", 20)

    print(timemap.get("love", 5))
    print(timemap.get("love", 10))
    print(timemap.get("love", 15))
    print(timemap.get("love", 20))
    print(timemap.get("love", 25))