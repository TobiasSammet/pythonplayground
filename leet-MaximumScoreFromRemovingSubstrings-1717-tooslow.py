class Solution:
    def getIndex(self, s: str, sub: str) -> int:
        try:
            return s.index(sub)
        except:
            return -1
        
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if len(s) < 2:
            return 0
        retVal: int = 0
        while len(s) > 0:
            print(s)
            ab = self.getIndex(s, "ab")
            ba = self.getIndex(s, "ab")
            if ab == -1 and ba == -1:
                break
            if x > y:
                if ab != -1:
                    while ab != -1:
                        s = s[:ab] + s[ab+2:]
                        retVal += x
                        ab = self.getIndex(s,"ab")
                else :
                    s = s[:ba] + s[ba+2:]
                    retVal += y
            else:
                if ba != -1:
                    while ba != -1:
                        print(ba)
                        print(s)
                        s = s[:ba] + s[ba+2:]
                        retVal += y
                        ba = self.getIndex(s,"ba")
                else :
                    s = s[:ab] + s[ab+2:]
                    retVal += x

        return retVal
    

thingy = Solution()


print(thingy.maximumGain('cdbcbbaaabab', 4, 5)) # 19
# print(thingy.maximumGain('aabbaaxybbaabb', 5, 4)) #20
# print(thingy.maximumGain())
# print(thingy.maximumGain())