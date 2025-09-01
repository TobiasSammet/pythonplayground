from typing import List

class Solution :
    count: int
    coins: List[int]
    coinCount: List[int]

    def change(self, amount: int, coins: List[int]) -> int :
        ways: List[int] = [0] * (amount + 1)
        ways[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    ways[i] = ways[i] + ways[i-coin]

        return ways[amount]

    def cchange(self, amount: int, coins: List[int]) -> int :
        if amount == 0:
            return 1
        if len(coins) == 0:
            return 0
        self.count = 0
        self.coins = coins
        self.coinCount = []
        for coin in coins:
            self.calcAmount(amount, coin, [])
        return self.count

    def calcAmount(self, amount: int, currentCoin: int, currentPath: List[int])  :
        tempAmount = amount - currentCoin
        currentPath.append(currentCoin)
        if tempAmount < 0:
            return
        if tempAmount == 0:
            tempCoinCount = len(currentPath)
            if tempCoinCount not in self.coinCount:
                self.coinCount.append(tempCoinCount)
                self.count += 1
                return
        for coin in self.coins:
            tempCurrentPath = currentPath.copy()
            self.calcAmount(tempAmount, coin, tempCurrentPath)

thing = Solution()
print(thing.change(5, [1,2,5]))
print(thing.change(500, [1,2,5]))