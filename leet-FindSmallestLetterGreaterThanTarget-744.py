# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

# Example 3:
# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

# Constraints:

#     2 <= letters.length <= 10^4
#     letters[i] is a lowercase English letter.
#     letters is sorted in non-decreasing order.
#     letters contains at least two different characters.
#     target is a lowercase English letter.

# Yes I know I should write a binary search algorithm (or at least make sure the last element is not too small)

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        value = ord(target)
        for letter in letters:
            if ord(letter) > value:
                return letter
        return letters[0]
    
def main(): 
    thingy = Solution()
    assert thingy.nextGreatestLetter(['c', 'f', 'j'], 'a') == "c", "Test case 1 failed"
    assert thingy.nextGreatestLetter(['c', 'f', 'j'], 'c') == "f", "Test case 2 failed"
    assert thingy.nextGreatestLetter(['x', 'x', 'y', 'y'], 'z') == "x", "Test case 3 failed"
    # assert thingy.nextGreatestLetter() == "", "Test case  failed"

if __name__ == "__main__":
    main()