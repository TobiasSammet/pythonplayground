class Solution:
    def minPartitions(self, n: str) -> int:
        length = len(n)
        if length == 0:
            return 0
        retVal: int = 0
        for char in n:
            retVal = max(retVal, int(char))
            if retVal == 9:
                return 9

        return retVal
    

def main():
    thingy = Solution()
    assert thingy.minPartitions("32") == 3, "Test Case Failed"
    assert thingy.minPartitions("82734") == 8, "Test Case Failed"
    assert thingy.minPartitions("27346209830709182346") == 9, "Test Case Failed"
    # assert thingy.minPartitions() == 1, "Test Case Failed"
    

if __name__ == "__main__":
    main()