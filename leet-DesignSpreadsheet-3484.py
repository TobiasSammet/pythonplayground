from typing import List
import re

class Spreadsheet:
    # declare and fill 2 dimensional array
    # declare and fill two dimensional array
    # arr = [[0 for i in range(cols)] for j in range(rows)]
    
    
    def __init__(self, rows: int):
        cols: int = 26
        self.spread = [[0 for i in range(cols)] for j in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        row = self.__mapTextToRow(cell)
        col = self.__mapTextToCol(cell)
        self.spread[row][col] = value

    def resetCell(self, cell: str) -> None:
        row = self.__mapTextToRow(cell)
        col = self.__mapTextToCol(cell)
        self.spread[row][col] = 0

    def getValue(self, formula: str) -> int:
        if formula[0] == "=":
            values: List[str] = formula[1:].split("+")
            val1: int = 0
            val2: int = 0
            if self.isSpreadText(values[0]):
                val1 = self.__getCell(values[0])
            else:
                val1 = int(values[0])
            if self.isSpreadText(values[1]):
                val2 = self.__getCell(values[1])
            else:
                val2 = int(values[1])

            return val1 + val2

        return 0

    def __mapTextToRow(self, cell: str) -> int:
        return int(cell[1:]) - 1
    
    def __mapTextToCol(self, cell: str) -> int:
        return ord(cell[0]) - ord('A')
    
    def isSpreadText(self, cell: str) -> bool:
        return re.match("[A-Z]\d+", cell) != None
    
    def __getCell(self, cell: str) -> int:
        row = self.__mapTextToRow(cell)
        col = self.__mapTextToCol(cell)
        return self.spread[row][col]


def main():
    spreadsheet: Spreadsheet = Spreadsheet(3); # Initializes a spreadsheet with 3 rows and 26 columns

    # print(spreadsheet.__mapTextToRow("A300")) # 299
    # print(spreadsheet.__mapTextToCol("M26")) # 12
    # print(spreadsheet.isSpreadText("Z01")) # True
    # print(spreadsheet.isSpreadText("240")) # False

    print(spreadsheet.getValue('=5+7')) # returns 12 (5+7)
    spreadsheet.setCell('A1', 10) # sets A1 to 10
    # print(spreadsheet.__getCell("A1")) # 10
    print(spreadsheet.getValue('=A1+6')) # returns 16 (10+6)
    spreadsheet.setCell('B2', 15) # sets B2 to 15
    # print(spreadsheet.__getCell("B2")) # 15
    print(spreadsheet.getValue('=A1+B2')) # returns 25 (10+15)
    spreadsheet.resetCell('A1') # resets A1 to 0
    # print(spreadsheet.__getCell("A1")) # 0
    print(spreadsheet.getValue('=A1+B2')) # returns 15 (0+15)
if __name__ == "__main__":
    main()    


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)