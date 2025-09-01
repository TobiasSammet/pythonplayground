from typing import List

class Solution: 
    def reverseString(self, s: List[str]) -> None:
        length: int = len(s)
        if length > 1:
            for i in range(length//2):
                temp: str = s[i]
                s[i] = s[length -i -1]
                s[length -i -1] = temp


thing = Solution()
s: List[str] = ["1", "2", "3", "4", "5"]
thing.reverseString(s)
print(s)