from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
        theStack = LifoQueue(maxsize=len(s))
        for i in range(0, len(s)):
            temp = s[i]
            if temp == "{" or temp == "[" or temp == "(":
                theStack.put(temp)
            else:
                if theStack.empty():
                    return False
                tempget = theStack.get()
                if temp == "}" and tempget != "{":
                    return False
                if temp == "]" and tempget != "[":
                    return False
                if temp == ")" and tempget != "(":
                    return False
        return theStack.empty()

thingy = Solution()

print(thingy.isValid("()")) # True
print(thingy.isValid("()[]{}")) # True
print(thingy.isValid("(])")) # False
print(thingy.isValid("([])")) # True
print(thingy.isValid("([)]")) # False
# print(thingy.isValid("")) # True