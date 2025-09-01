class Solution :
    def hammingDistance(self, x: int, y: int) -> int :
        res: int = 0
        while x > 0 or y > 0 :
            if x%2 != y%2 :
                
                res=res+1
            x = x//2
            y = y//2

        return res

thing = Solution()
print(thing.hammingDistance(1,4)) #2