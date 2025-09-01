from typing import List


class Solution:
    def frequencySort(self, s: str) -> str:
        retVal: str = ""
        if len(s) <= 1:
            return s
        lookup: dict[str, int] = {}
        for c in s:
            if c in lookup:
                lookup[c] += 1
            else:
                lookup[c] = 1
        maxValue: int = max(lookup.values())
        for i in range(maxValue, 0, -1):
            for key in lookup.keys():
                if lookup[key] == i:
                    for j in range(i):
                        retVal += key
        return retVal

thing = Solution()
print(thing.frequencySort('Matt'))