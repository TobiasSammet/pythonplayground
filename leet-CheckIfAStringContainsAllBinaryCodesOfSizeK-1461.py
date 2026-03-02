class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        length: int = len(s)
        # 2^k + k - 1 -- string must be this long to possibly have all the strings
        if length < (pow(2, k) + k - 1):
            return False
        
        retVal = set()
        for i in range(length -k + 1):
            retVal.add(s[i:i+k])
        
        return len(retVal) == pow(2, k)
    

def main():
    thingy = Solution()
    assert thingy.hasAllCodes('00110', 2) == True, "Test Case Failed"
    assert thingy.hasAllCodes('00110110', 2) == True, "Test Case Failed"
    assert thingy.hasAllCodes('0110', 2) == False, "Test Case Failed"
    assert thingy.hasAllCodes( \
        '011111011101111000010111100001011010010011010100100111101101011010111011011100110001011010001000100110010000101010000000111000010001011001110011100000100101000011110010000101001111110001001010111000011010011111111100011110000111110101101', \
        18) == False, "Test Case Failed"
    # assert thingy.hasAllCodes("", ) == False, "Test Case Failed"




if __name__ == "__main__":
    main()