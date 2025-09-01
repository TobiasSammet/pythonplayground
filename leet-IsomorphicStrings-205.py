class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        length: int = len(s)
        letters = dict()
        letters2 = dict()
        for i in range(0, length):
            if letters.get(s[i]):
                if letters[s[i]] != t[i]:
                    return False
            else:
                if letters2.get(t[i]):
                    if letters2[t[i]] != s[i]:
                        return False
            letters[s[i]] = t[i]
            letters2[t[i]] = s[i]
        return True

def main():
    thingy = Solution()
    print(thingy.isIsomorphic('egg', 'add')) # True
    print(thingy.isIsomorphic('foo', 'bar')) # False
    print(thingy.isIsomorphic('paper', 'title')) # True
    print(thingy.isIsomorphic('badc', 'baba')) # False
    # print(thingy.isIsomorphic()) # 
    
if __name__ == "__main__":
    main()