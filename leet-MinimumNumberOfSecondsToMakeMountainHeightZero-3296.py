from typing import List
import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        if mountainHeight == 0:
            return 0
        length: int = len(workerTimes)
        longest_time: int = max(workerTimes)
        longest_time_possible: int = math.ceil((longest_time * mountainHeight * (mountainHeight + 1)) / 2)
        if length == 1: 
            return longest_time_possible
        min_value: int = 1
        max_value: int = longest_time_possible
        ret_val: int = 0
        while min_value <= max_value:
            current_value: int = math.floor((min_value + max_value) /2)
            temp_height: int = 0
            for value in workerTimes:
                work: int = math.floor(current_value / value)
                k: int = math.floor((-1.0 + math.sqrt(1 + work * 8)) / 2)
                temp_height += k
            if temp_height >= mountainHeight:
                ret_val = current_value
                max_value = current_value - 1
            else:
                min_value = current_value + 1


        return ret_val
    

def main():
    thingy = Solution()
    assert thingy.minNumberOfSeconds(4, [2, 1, 1]) == 3, "Test Case Failed"
    assert thingy.minNumberOfSeconds(10, [3, 2, 2, 4]) == 12, "Test Case Failed"
    assert thingy.minNumberOfSeconds(5, [1]) == 15, "Test Case Failed"
    assert thingy.minNumberOfSeconds(10000, [1]) == 50005000, "Test Case Failed"
    # assert thingy.minNumberOfSeconds() == , "Test Case Failed"

if __name__ == "__main__":
    main()         