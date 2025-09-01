from typing import List

class Solution :
    def distributeCandies(self, candies: int, num_people: int) -> List[int] :
        retVal: List[int] = [0] * num_people
        tempCandies: int = candies
        i: int = 0
        while True: 
            retVal[i % num_people] += min(i+1, candies)
            candies = candies - (i+1)
            if candies <= 0: 
                break
            i+=1
        
        return retVal
thing = Solution()
print(thing.distributeCandies(7,4))
print(thing.distributeCandies(10,3))