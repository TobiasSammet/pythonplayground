# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"

# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"

# Example 3:
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"

# Constraints:

#     -231 <= numerator, denominator <= 231 - 1
#     denominator != 0
import math

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        starter = self.__sign(numerator) * self.__sign(denominator)
        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient = math.floor(numerator/denominator)
        remainder = numerator - (quotient * denominator)
        retVal = ""
        if starter == -1:
            retVal += "-"
        retVal += str(quotient)
        if remainder == 0:
            return retVal
        
        retVal += "."
        # perform long division until it terminates of a repeating pattern is found 
        remainders = dict()
        while remainder > 0:
            if remainder in remainders:
                index = remainders[remainder]
                retVal = retVal[:index] + "(" + retVal[index:] + ")"
                retVal = retVal
                break
            remainders[remainder] = len(retVal)

            remainder *= 10
            while remainder < denominator :
                remainder *= 10
                retVal += "0"
            
        
            quotient = math.floor(remainder/ denominator)
            remainder -= (denominator * quotient)
            retVal += str(quotient)

        # return retVal

    def __sign(self, num):
        return -1 if num < 0 else 1
    def otraVez(self) -> num:
        return 22
    


def main():
    thingy = Solution()
    print(thingy.fractionToDecimal(1,2)) # 0.5
    print(thingy.fractionToDecimal(2,1)) # 2
    print(thingy.fractionToDecimal(4, 333)) # 0.(012)
    print(thingy.fractionToDecimal(1,11)) # 0.(09)
    # print(thingy.fractionToDecimal()) # 
    

if __name__ == "__main__":
    main()         