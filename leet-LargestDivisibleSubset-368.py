from typing import List

def printList(myList: List[int]) :
    retVal: str = ""
    for item in myList:
        retVal += " " + str(item) + " ->"
    print(retVal)


class Solution :
    def largestDivisibleSubset(self, nums: List[int]) -> List[int] :
        retVal: List[int] = []
        length: int = len(nums)
        if length == 0:
            return retVal
        count: List[int] = [1] * length
        numbers: List[int] = nums.copy()
        numbers.sort()
        
        # step 2 for each element in nums find the length of the largest subset it has
        for i in range(1,length):
            for j in range(i-1, -1, -1):
                if numbers[i] % numbers[j] == 0:
                    count[i] = max(count[i], count[j] + 1)

        # step 3 pick the index of the largest element in count.
        maxIndex: int = 0
        for i in range(1, length):
            maxIndex = i if count[i] > count[maxIndex] else maxIndex

        # step 4 from nums[maxIndex] to 0, add every element belongs to the largest subset.          
        temp: int = numbers[maxIndex]
        currentCount: int = count[maxIndex]
        for i in range(maxIndex, -1, -1):
            if temp % numbers[i] == 0 and count[i] == currentCount :
                retVal.append(numbers[i])
                temp = numbers[i]
                currentCount  -= 1
        
        retVal.sort() 

        
        return retVal




thing = Solution()
nums: List[int] = [2,3,4,9,8]
print(thing.largestDivisibleSubset(nums))