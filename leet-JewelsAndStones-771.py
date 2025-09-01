class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if J == '' or S == '' :
            return 0
        jewelTypes: set = set()
        for c in J :
            if not (c in jewelTypes) :
                jewelTypes.add(c)
        count: int = 0
        for c in S :
            if c in jewelTypes:
                count = count + 1

        return count

thing = Solution()

print(thing.numJewelsInStones('aA', 'aAAbbbb'))