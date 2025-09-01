from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        retVal: int = 0
        myset = set()
        for num in arr :
            myset.add(num)

        for num in arr :
            if num + 1 in myset:
                retVal += 1

        return retVal

thing = Solution()
list: List[int] = [1,3,2,3,5,0]
print(thing.countElements(list))
