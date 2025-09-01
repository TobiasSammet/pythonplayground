import sys
class Solution :
    def buddyStrings(self, A: str, B:str) -> bool :
        firstDiff: int = -sys.maxsize
        secondDiff: int = -sys.maxsize
        if len(A) != len(B):
            return False
        numDiffs: int = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                numDiffs += 1
                if numDiffs > 2 :
                    return False
                if firstDiff == -sys.maxsize :
                    firstDiff = i
                else :
                    secondDiff = i
        if numDiffs != 0 and numDiffs != 2:
            return False
        if numDiffs == 0:
            return self.calcWithZeroDifferences(A)
        first: str = A
        temp1: str = A[firstDiff]
        temp2: str = A[secondDiff]
        first = A[0: firstDiff] + temp2 + A[firstDiff + 1: secondDiff] + temp1 + A[secondDiff + 1:]
        

        return first == B

    def calcWithZeroDifferences(self, theString: str) -> bool :
        if len(theString) == 0:
            return False
        lengthOfString: int = len(theString)
        for i in range(lengthOfString -1):
            for j in range(1, lengthOfString):
                if i != j:
                    if theString[i] == theString[j]:
                        return True
        return False


thing = Solution()
# print(thing.buddyStrings("aaaaaaabc","aaaaaaacb"))
# print(thing.buddyStrings("aaaaaaa","aaaaaaa"))
# print(thing.buddyStrings("aaaaaaabd","aaaaaaacb"))
print(thing.buddyStrings("ab","ab"))
print(thing.buddyStrings("aba","aba"))