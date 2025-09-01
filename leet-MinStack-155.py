from typing import List

class MinStack:
    stack: List[int] = []
    minValues: List[int] = []

    def __init__(self):
        """
        initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minValues) == 0 or self.minValues[len(self.minValues) -1 ] > x :
            self.minValues.append(x)
        else :
            self.minValues.append(self.minValues[len(self.minValues) -1])            

    def pop(self) -> None:
        self.stack.pop()
        self.minValues.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) -1 ]

    def getMin(self) -> int:
        return self.minValues[len(self.minValues) -1 ]

thing = MinStack()
thing.push(-2)
thing.push(0)
thing.push(-3)
print(thing.getMin()) # -3
thing.pop()
print(thing.top()) # 0
print(thing.getMin()) # -2