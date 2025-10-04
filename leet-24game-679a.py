from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        length = len(cards)
        EPS = 1e-6
        if length == 1:
            return abs(cards[0] - 24.0) < EPS
        for i in range(0, length):
            for j in range(0,length):
                if i == j:
                    continue
                newNums = cards.copy()
                a = newNums[i]
                b = newNums[j]
                if i > j:
                    newNums.pop(i)
                    newNums.pop(j)
                else: 
                    newNums.pop(j)
                    newNums.pop(i)
                if b == 0:
                    if (self.judgePoint24(self.addValueToList(a+b, newNums)) or  
                        self.judgePoint24(self.addValueToList(a-b, newNums)) or 
                        self.judgePoint24(self.addValueToList(a*b, newNums))):
                        return True
                elif (self.judgePoint24(self.addValueToList(a+b, newNums)) or 
                      self.judgePoint24(self.addValueToList(a-b, newNums)) or 
                      self.judgePoint24(self.addValueToList(a*b, newNums)) or 
                      self.judgePoint24(self.addValueToList(a/b, newNums))):
                    return True
        return False
    
    def addValueToList(self, newValue: int, cards: List[int]) -> List[int]:
        newNums: List[int] = cards.copy()
        newNums.append(newValue)
        return newNums

thingy = Solution()

print(thingy.judgePoint24([1,2,1,2])) # False
print(thingy.judgePoint24([4,1,8,7])) # True
print(thingy.judgePoint24([3,3,8,8])) # True
print(thingy.judgePoint24([1,7,4,5])) # True
print(thingy.judgePoint24([1,3,4,6])) # True
print(thingy.judgePoint24([1,9,1,2])) # True
# print(thingy.judgePoint24([])) #