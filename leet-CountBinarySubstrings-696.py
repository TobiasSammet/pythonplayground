# Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.

# Example 1:
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

# Example 2:
# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

# Constraints:
#     1 <= s.length <= 10^5
#     s[i] is either '0' or '1'.

# This problem is a little bit tricky but the solution is easy and straightforward:

#     Think of it as you want to count each one untill you find a zero then store this count.
#     Then count each zero untill you find a one then store this count.
#     Then:
#     Count valid substrings: For each pair of consecutive groups, the number of valid substrings is the minimum of the lengths of the two groups.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        length = len(s)
        if length <= 1:
            return 0
        retVal: int = 0
        zeroCount: int = 0
        oneCount: int = 0
        flip: bool = False

        starter: int = s.find("0")

        if starter >= 0:
            for i in range(starter, length):
                tempVal = s[i]
                if tempVal == '0':
                    if flip:
                        # take the count
                        flip = False
                        retVal += min(zeroCount, oneCount)
                        zeroCount = 1
                        oneCount = 0
                    else:
                        zeroCount += 1
                else:
                    flip = True
                    oneCount += 1
            retVal += min(zeroCount, oneCount)

        starter: int = s.find("1")

        if starter >= 0:
            zeroCount = 0
            oneCount = 0
            flip = False
            for i in range(starter, length):
                tempVal = s[i]
                if tempVal == '1':
                    if flip:
                        # take the count
                        flip = False
                        retVal += min(zeroCount, oneCount)
                        oneCount = 1
                        zeroCount = 0
                    else:
                        oneCount += 1
                else:
                    flip = True
                    zeroCount += 1
            retVal += min(zeroCount, oneCount)
        return retVal



def main():
    thingy = Solution()
    assert thingy.countBinarySubstrings("00110011") == 6, "Test case failed"
    assert thingy.countBinarySubstrings("10101") == 4, "Test case failed"
    assert thingy.countBinarySubstrings("00110") == 3, "Test case failed"
    assert thingy.countBinarySubstrings("00") == 0, "Test case failed"
    assert thingy.countBinarySubstrings("11") == 0, "Test case failed"
    assert thingy.countBinarySubstrings("00100") == 2, "Test case failed"
    # assert thingy.countBinarySubstrings() == 1, "Test case failed"
    
if __name__ == "__main__":
    main()