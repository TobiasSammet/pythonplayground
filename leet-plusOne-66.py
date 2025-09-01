from typing import List

class Solution :
    def plusOne(self, digits: List[int]) -> List[int] :
        digits.reverse()
        carryOver: bool = False
        for i in range(len(digits)) :
            if digits[i] != 9:
                digits[i] +=1
                carryOver = False
                break
            digits[i] = 0
            carryOver = True
        
        if carryOver :
            digits.append(1)

        digits.reverse()
        return digits

thing = Solution()
print(thing.plusOne([1,2,3]))
print(thing.plusOne([1,2,9]))
print(thing.plusOne([9,9,9]))