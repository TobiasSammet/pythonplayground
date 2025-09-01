class VersionControl: 
    def isBadVersion(self, n: int) -> bool:
        if n >= 56 :
            return True
        return False

class Solution(VersionControl):
    pass
    def firstBadVersion(self, n) -> int:
        if n <= 1 :
            return n
        increment: int = n // 2
        cutSpot: int = increment
        while True:
            increment = increment // 2
            if self.isBadVersion(cutSpot):
                cutSpot -= increment
            else:
                cutSpot += increment
            if increment <= 1:
                break
        
        if self.isBadVersion(cutSpot):
            while self.isBadVersion(cutSpot):
                cutSpot -=1
            cutSpot += 1
        else:
            while not self.isBadVersion(cutSpot):
                cutSpot += 1
            
        return cutSpot


thing = Solution()
print(thing.firstBadVersion(100))