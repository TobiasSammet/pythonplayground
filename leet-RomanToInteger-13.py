class Solution:
    def romanToInt(self, s: str) -> int:
        retVal: int = 0

        i : int = 0

        while i < len(s):
            nextTwo = s[i:i+2]
            match nextTwo:
                case "IV":
                    retVal += 4
                    i += 2
                case "IX":
                    retVal += 9
                    i += 2
                case "XL":
                    retVal += 40
                    i += 2
                case "XC":
                    retVal += 90
                    i += 2
                case "CD":
                    retVal += 400
                    i += 2
                case "CM":
                    retVal += 900
                    i += 2
                case "IX":
                    retVal += 9
                    i += 2
                case _:
                    match s[i]:
                        case "I":
                            retVal += 1
                            i +=1
                        case "V":
                            retVal += 5
                            i +=1
                        case "X":
                            retVal += 10
                            i +=1
                        case "L":
                            retVal += 50
                            i +=1
                        case "C":
                            retVal += 100
                            i +=1
                        case "D":
                            retVal += 500
                            i +=1
                        case "M":
                            retVal += 1000
                            i +=1
                        
            

        return retVal
    


thingy = Solution()

print(thingy.romanToInt("III")) # 3
print(thingy.romanToInt("LVIII")) # 58
print(thingy.romanToInt("MCMXCIV")) # 1994
print(thingy.romanToInt("DCXXI")) #621
# print(thingy.romanToInt()) #