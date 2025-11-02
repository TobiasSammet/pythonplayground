from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        expectedNum: int = 0
        retVal: List[int] = []
        for num in nums:
            if num == expectedNum:
                expectedNum += 1
            else:
                retVal.append(num)
                if len(retVal) == 2:
                    return retVal
                
        return retVal
    

def main(): 
    thingy = Solution()

    print(thingy.getSneakyNumbers([0, 1, 1, 0])) # [0,1]
    print(thingy.getSneakyNumbers([0, 3, 2, 1, 3, 2])) # [2,3]
    print(thingy.getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2])) #[4,5]
    # print(thingy.getSneakyNumbers()) #
    


if __name__ == "__main__":
    main()    