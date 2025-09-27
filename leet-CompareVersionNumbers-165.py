# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
# To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.
# Return the following:
#     If version1 < version2, return -1.
#     If version1 > version2, return 1.
#     Otherwise, return 0.

# Example 1:
# Input: version1 = "1.2", version2 = "1.10"
# Output: -1
# Explanation:
# version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

# Example 2:
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation:
# Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

# Example 3:
# Input: version1 = "1.0", version2 = "1.0.0.0"
# Output: 0
# Explanation:
# version1 has less revisions, which means every missing revision are treated as "0".

# Constraints:

#     1 <= version1.length, version2.length <= 500
#     version1 and version2 only contain digits and '.'.
#     version1 and version2 are valid version numbers.
#     All the given revisions in version1 and version2 can be stored in a 32-bit integer.



class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        one = version1.split(".")
        two = version2.split(".")
        lenOne = len(one)
        lenTwo = len(two)
        maxlen = max(lenOne, lenTwo)
        
        for i in range(0, maxlen):
            temp1 = temp2 = 0
            if i < lenOne:
                temp1 = int(one[i])
            if i < lenTwo:
                temp2 = int(two[i])
            if temp1 < temp2:
                return -1
            if temp1 > temp2:
                return 1
        return 0
    

def main():
    thingy = Solution()
    print(thingy.compareVersion('1.2', '1.10')) # -1
    print(thingy.compareVersion('1.01', '1.0001')) # 0
    print(thingy.compareVersion('1.0', '1.0.0.0')) # 0
    print(thingy.compareVersion('10.1.1', '10.1')) # 1
    print(thingy.compareVersion("12", "10"))
    # print(thingy.compareVersion()) # 
    

if __name__ == "__main__":
    main()    