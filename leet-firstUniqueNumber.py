from typing import List
from typing import Dict

class FirstUnique:
    theNums: List[int]
    uniqueValues: Dict[int, int] = {}

    def __init__(self, nums: List[int]):
        self.theNums = nums
        for num in self.theNums:
            self.add(num, False)

    def showFirstUnique(self) -> int:
        for num in self.theNums:
            if num in self.uniqueValues and self.uniqueValues[num] == 1:
                return num
        return -1

    def add(self, value: int, append: bool = True) -> None:
        if value in self.uniqueValues :
            self.uniqueValues[value] = self.uniqueValues.get(value) + 1
        else :
            self.uniqueValues[value] = 1
        if append:    
            self.theNums.append(value)
        # self.theNums.append(value)


nums: List[int] = [2,3,5]


thing = FirstUnique(nums)
print(thing.showFirstUnique())
thing.add(5)
print(thing.showFirstUnique())
thing.add(2)
print(thing.showFirstUnique())
thing.add(3)
print(thing.showFirstUnique())

