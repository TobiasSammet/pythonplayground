from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        length: int = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        myClonedArray = nums.copy()
        for i in range(0, length-1):
            temp: List[int] = [0] * (length -i -1)
            for j in range(0, (length -i -1)):
                temp[j] = (myClonedArray[j] + myClonedArray[j+1])% 10
            myClonedArray = temp.copy()
        return myClonedArray[0]




def main():
    thingy = Solution()
    print(thingy.triangularSum([1,2,3,4,5])) # 8
    print(thingy.triangularSum([5])) # 5
    # print(thingy.triangularSum()) # 


if __name__ == "__main__":
    main()