from typing import List
import collections

class Solution :
    def topKFrequent(self, nums: List[int], k: int) -> List[int] :
        retval: List[int] = []
        cache: collections.defaultdict = collections.defaultdict()
        for item in nums:
            if item in cache:
                cache[item] = cache[item] + 1
            else:
                cache[item] = 1
        count: int = 0
        for x in sorted(cache, key=cache.get, reverse = True) :
            # print(x)
            retval.append(x)
            count += 1
            if count >= k:
                break
        
        
        return retval

thing = Solution()
nums: List[int] = [1,1,1,2,2,3,3,3,3]
print(thing.topKFrequent(nums, 2))