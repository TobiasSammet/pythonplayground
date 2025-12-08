from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        rightSum: int = sum(nums)
        leftSum: int = 0
        retVal: int = 0

        for i in range(0, len(nums) -1):
            leftSum += nums[i]
            rightSum -= nums[i]
            if (leftSum - rightSum) % 2 == 0:
                retVal += 1
        return retVal
    

def main():
    thingy = Solution()
    print(thingy.countPartitions([10, 10, 3, 7, 6])) # 4
    print(thingy.countPartitions([1, 2, 2])) # 0
    print(thingy.countPartitions([2, 4, 6, 8])) # 3
    # print(thingy.countPartitions()) # 
    # print(thingy.countPartitions()) # 
    # print(thingy.countPartitions()) # 

if __name__ == "__main__":
    main()