import math

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        larger: int = max(n,m)
        smaller: int = min(n,m)
        largerEvens: int = 0
        largerOdds: int = 0
        smallerEvens: int = 0
        smallerOdds: int = 0

        if larger % 2 == 0:
            largerEvens = larger/2
            largerOdds = math.ceil(larger/2)
        else :
            largerEvens = math.floor(larger / 2)
            largerOdds = math.ceil(larger / 2)
        
        if smaller % 2 == 0:
            smallerEvens = smaller/2
            smallerOdds = math.ceil(smaller/2)
        else :
            smallerEvens = math.floor(smaller / 2)
            smallerOdds = math.ceil(smaller / 2)
        

        return math.floor(largerOdds * smallerEvens + largerEvens * smallerOdds)
    
def main():
    thingy = Solution()
    print(thingy.flowerGame(3,2)) # 3
    print(thingy.flowerGame(1,1)) # 0
    print(thingy.flowerGame(1,5)) # 2
    # print(thingy.flowerGame()) # 
    # print(thingy.flowerGame()) # 

if __name__ == "__main__":
    main()