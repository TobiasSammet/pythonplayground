from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        if (len(players) == 0)or (len(trainers) == 0):
            return 0
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        # print(players)
        # print(trainers)
        retVal: int = 0
        j: int = 0
        for value in trainers:
            while j < len(players):
                if players[j] <= value:
                    retVal += 1
                    j+=1
                    break
                j +=1
            if j > len(players):
                return retVal

        return retVal
    

thingy = Solution()

print(thingy.matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]))
print(thingy.matchPlayersAndTrainers([1,1,1], [10]))
# print(thingy.matchPlayersAndTrainers([], []))