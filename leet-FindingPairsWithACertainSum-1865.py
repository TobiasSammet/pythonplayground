from typing import List

class FindSumPairs:
    nums1: List[int]
    nums2: List[int]
    cache: dict

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cache = {}
        for val in nums2:
            if val in self.cache:
                tempVal = self.cache.get(val)
                self.cache[val] = tempVal + 1
            else:
                self.cache[val] = 1

        

    def add(self, index: int, val: int) -> None:
        oldVal: int = self.nums2[index]
        newVal: int = oldVal + val
        self.nums2[index] += val
        self.cache[oldVal] -= 1
        if newVal in self.cache:
            self.cache[newVal] += 1
        else:
            self.cache[newVal] = 1


        

    def count(self, tot: int) -> int:
        retVal: int = 0
        for val1 in self.nums1:
            if val1 < tot:
                tempVal = tot - val1
                if tempVal in self.cache:
                    retVal += self.cache[tempVal]
        return retVal

# too slow
# class FindSumPairs:
#     nums1: List[int]
#     nums2: List[int]

#     def __init__(self, nums1: List[int], nums2: List[int]):
#         self.nums1 = nums1
#         self.nums2 = nums2
        

#     def add(self, index: int, val: int) -> None:
#         self.nums2[index] += val
        

#     def count(self, tot: int) -> int:
#         retVal: int = 0
#         for val1 in self.nums1:
#             for val2 in self.nums2:
#                 if val1 + val2 == tot:
#                     retVal += 1
#         return retVal
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

findSumPairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])

# pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
print(findSumPairs.count(7)) # return 8;
findSumPairs.add(3, 2); # now nums2 = [1,4,5,4,5,4]
print(findSumPairs.count(8)) # return 2; pairs (5,2), (5,4) make 3 + 5
print(findSumPairs.count(4)) # return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1); # now nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1); # now nums2 = [2,5,5,4,5,4]

# pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4
print(findSumPairs.count(7)) # return 11;

