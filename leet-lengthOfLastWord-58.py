class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if s is None:
            return 0
        s = s.strip()
        if len(s) == 0:
            return 0
        if s.find(' ') == -1:
            return len(s)
        myList = s.split()
        print(myList)
        i = len(myList)

        return len(myList[i-1])

thing = Solution()
print(thing.lengthOfLastWord(' Matt was here'))
print(thing.lengthOfLastWord('Matt was here'))