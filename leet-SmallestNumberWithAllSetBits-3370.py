# You are given a positive number n.
# Return the smallest number x greater than or equal to n, such that the binary representation of x contains only

# Example 1:
# Input: n = 5
# Output: 7
# Explanation:
# The binary representation of 7 is "111".

# Example 2:
# Input: n = 10
# Output: 15
# Explanation:
# The binary representation of 15 is "1111".

# Example 3:
# Input: n = 3
# Output: 3
# Explanation:
# The binary representation of 3 is "11".

# Constraints:
#     1 <= n <= 1000

class Solution:
    def smallestNumber(self, n: int) -> int:
        temp: str = "{0:b}".format(n)
        temp = temp.replace('0', '1')
        # print(temp)
        return int(temp, 2)
    


def main(): 
    thingy = Solution()
    print(thingy.smallestNumber(5)) # 7
    print(thingy.smallestNumber(10)) # 15
    print(thingy.smallestNumber(3)) # 3
    # print(thingy.smallestNumber()) # 
    # print(thingy.smallestNumber()) # 


if __name__ == "__main__":
    main()