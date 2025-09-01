from typing import List

class Solution(object):
    ans: List[List[int]] = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        currentListOfUnusedValues: List[int] = nums.copy()
        for num in nums :
            currentList: List[int]=[]
            self.getNextPermutation(currentList,num,currentListOfUnusedValues);     
        return self.ans

    def getNextPermutation(self, currentList: List[int], num: int, currentListOfUnusedValues: List[int]) :
        newCurrentList: List[int] = currentList.copy()
        newCurrentListOfUnusedValues: List[int] = currentListOfUnusedValues.copy()
        newCurrentList.append(num)
        newCurrentListOfUnusedValues.remove(num)
        if len(newCurrentListOfUnusedValues) == 0 :
            self.ans.append(newCurrentList)
        else : 
            for theNum in newCurrentListOfUnusedValues :
                self.getNextPermutation(newCurrentList, theNum, newCurrentListOfUnusedValues)


thing = Solution()
nums: List[int] = [1,2,3]
print(thing.permute(nums))