from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        first: bool = False
        second:bool = False
        # print(first, second)
        for num in arr:
            if num % 2 == 1:
                if first:
                    if second:
                        return True
                    else:
                        second = True
                else:
                    first = True
                    second = False
            else:
                first = False
                second = False
        
        return False
    

thing = Solution()
print(thing.threeConsecutiveOdds([4,3,2,7,8,2,3,1]))
print(thing.threeConsecutiveOdds([1,3,5,4,3,2,7,8,2,3,1]))
print(thing.threeConsecutiveOdds([4,3,2,7,8,2,3,1,5]))