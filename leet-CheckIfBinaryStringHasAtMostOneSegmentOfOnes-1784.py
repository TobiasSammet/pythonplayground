# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

# Example 1:
# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.

# Example 2:
# Input: s = "110"
# Output: true

# Constraints:
#     1 <= s.length <= 100
#     s[i]​​​​ is either '0' or '1'.
#     s[0] is '1'.

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        length: int = len(s)
        flip_the_switch: bool = False
        for i in range(length):
            if s[i] == "0":
                flip_the_switch = True
            if flip_the_switch and s[i] == "1":
                return False

        return True
    
def main():
    thingy = Solution()
    assert thingy.checkOnesSegment("1001") == False, "Test Case Failed"
    assert thingy.checkOnesSegment("110") == True, "Test Case Failed"
    # assert thingy.checkOnesSegment("") == True, "Test Case Failed"



if __name__ == "__main__":
    main()          