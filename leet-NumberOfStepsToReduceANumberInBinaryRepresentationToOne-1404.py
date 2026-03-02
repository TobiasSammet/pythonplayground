# Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
#     If the current number is even, you have to divide it by 2.
#     If the current number is odd, you have to add 1 to it.
# It is guaranteed that you can always reach one for all test cases.

# Example 1:
# Input: s = "1101"
# Output: 6
# Explanation: "1101" corressponds to number 13 in their decimal representation.
# Step 1) 13 is odd, add 1 and obtain 14.
# Step 2) 14 is even, divide by 2 and obtain 7.
# Step 3) 7 is odd, add 1 and obtain 8.
# Step 4) 8 is even, divide by 2 and obtain 4.
# Step 5) 4 is even, divide by 2 and obtain 2.
# Step 6) 2 is even, divide by 2 and obtain 1.

# Example 2:
# Input: s = "10"
# Output: 1
# Explanation: "10" corresponds to number 2 in their decimal representation.
# Step 1) 2 is even, divide by 2 and obtain 1.

# Example 3:
# Input: s = "1"
# Output: 0

# Constraints:
#     1 <= s.length <= 500
#     s consists of characters '0' or '1'
#     s[0] == '1'


# from decimal import Decimal, getcontext

class Solution:

    # this blows up on the last test case :()
    # def numSteps(self, s: str) -> int:
    #     ret_val:int = 0
    #     temp_num = int(s, 2)
    #     the_num = Decimal(temp_num)
    #     while the_num != 1:
    #         ret_val += 1
    #         if the_num % 2 == 1:
    #             the_num+=1
    #         else:
    #             the_num = the_num / 2

    #     return ret_val
    
    def numSteps(self, s: str) -> int:
        retVal:int = 0
        while s != '1':
            if s[-1] == "0":
                retVal += 1
                s = s[:-1]
            else:
                retVal += 1
                temp_str: str = "0"
                length = len(s)
                i: int = length -2
                while s[i] != "0" and i >= 0:
                    temp_str = "0" + temp_str
                    i -=1
                if i == -1:
                    s = "1" + temp_str
                else:
                    s = s[:i] + "1" + temp_str
        return retVal
    

def main():
    thingy = Solution()
    # assert thingy.numSteps("1101") == 6, "Test Case Failed"
    # assert thingy.numSteps("10") == 1, "Test Case Failed"
    # assert thingy.numSteps("1") == 0, "Test Case Failed"
    # assert thingy.numSteps("1111011110000011100000110001011011110010111001010111110001") == 85, "Test Case Failed"
    assert thingy.numSteps("1100100000101010001001100101111110100101110010000010001011101101100000101000110000100000111000001111") == 158, "Test Case Failed"


if __name__ == "__main__":
    main()