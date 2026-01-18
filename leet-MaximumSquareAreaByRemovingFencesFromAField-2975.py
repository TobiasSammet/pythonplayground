# There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal and vertical fences given in arrays hFences and vFences respectively.
# Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).
# Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is impossible to make a square field.
# Since the answer may be large, return it modulo 109 + 7.
# Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.

# Example 1:
# Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
# Output: 4
# Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.

# Example 2:
# Input: m = 6, n = 7, hFences = [2], vFences = [4]
# Output: -1
# Explanation: It can be proved that there is no way to create a square field by removing fences.

# Constraints:
#     3 <= m, n <= 109
#     1 <= hFences.length, vFences.length <= 600
#     1 < hFences[i] < m
#     1 < vFences[i] < n
#     hFences and vFences are unique.

# Calculate all distances between fences (horizontal), remebering first to add fences at the permieter of the field
# The loop through vertical to find largest differejnce which exists in the horizontal ones
# that modulo though was a bear

from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        modulo = (10**9 + 7) # MOD
        if m == n:
            return ((m-1) * (n-1)) % modulo
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)
        retVal: int = -1
        hSet = set()
        for i in range(0, len(hFences)):
            for j in range(0, len(hFences)):
                if i != j:
                    distance: int = abs(hFences[i]- hFences[j])
                    hSet.add(distance)

        for i in range(0, len(vFences)):
            for j in range(0, len(vFences)):
                if i != j:
                    distance: int = abs(vFences[i]- vFences[j])
                    if distance in hSet:
                        retVal = max(retVal, distance)

        if retVal == -1:
            return -1
        return (retVal * retVal) % modulo
    

def main(): 
    thingy = Solution()
    assert thingy.maximizeSquareArea(4, 3, [2, 3], [2]) == 4, "Test case 1 failed"
    assert thingy.maximizeSquareArea(6, 7, [2], [4]) == -1, "Test case 2 failed"
    assert thingy.maximizeSquareArea(4, 4, [2], [2, 3]) == 9, "Test case 3 failed"


if __name__ == "__main__":
    main()