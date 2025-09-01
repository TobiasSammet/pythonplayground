class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(0, len(s)):
            temp: str = s[i]
            if temp == '1':
                continue
            if s.find(temp, i+1) == -1 :
                return i
            s = s.replace(temp, "1")
        return -1


thing = Solution()
print(thing.firstUniqChar('leetcode')) # 0
print(thing.firstUniqChar('loveleetcode')) # 2
print(thing.firstUniqChar('cc')) # -1
