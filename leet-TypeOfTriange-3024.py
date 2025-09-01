# You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

#     A triangle is called equilateral if it has all sides of equal length.
#     A triangle is called isosceles if it has exactly two sides of equal length.
#     A triangle is called scalene if all its sides are of different lengths.

# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

 

# Example 1:

# Input: nums = [3,3,3]
# Output: "equilateral"
# Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.

# Example 2:

# Input: nums = [3,4,5]
# Output: "scalene"
# Explanation: 
# nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
# nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
# nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. 
# Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
# As all the sides are of different lengths, it will form a scalene triangle.


from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if min(nums) <= 0:
            return "none"
        
        if nums[0] == nums[1] == nums[2]:
            return  "equilateral"

        # length of the biggest side should be smaller than the two remaining sides
        maxSide = 0
        remainingSides = 0
        for value in nums:
            if value > maxSide:
                remainingSides += maxSide
                maxSide = value
            else:
                remainingSides += value

        if (maxSide >= remainingSides): 
            return "none"


        if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return "isosceles"
        
        
        return "scalene"
        

thingy = Solution()

print(thingy.triangleType([5,3,8]))
print(thingy.triangleType([3,3,3]))
print(thingy.triangleType([1,3,3]))
print(thingy.triangleType([1,2,3]))
print(thingy.triangleType([8,4,2]))

