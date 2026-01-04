class Solution:
    def bestClosingTime(self, customers: str) -> int:
        if customers == "N":
            return 0
        length: int = len(customers)
        if length == 0:
            return 0
        currentDay: int = 0
        maxValue: int = 0
        currentValue: int = 0

        for i in range(0, length):
            if customers[i] == "Y":
                currentValue += 1
            else:
                currentValue -= 1
            if currentValue > maxValue:
                maxValue = currentValue
                currentDay = i + 1
        return currentDay
    

def main(): 
    thingy = Solution()
    print(thingy.bestClosingTime("YYNY")) # 2
    print(thingy.bestClosingTime("NNNNN")) # 0
    print(thingy.bestClosingTime("YYYY")) # 4
    # print(thingy.bestClosingTime()) # 

    assert thingy.bestClosingTime("YYNY") == 2, "Test Case 1 failed"
    

if __name__ == "__main__":
    main()