# You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.
# You can apply either of the following two operations any number of times and in any order on s:
#     Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, if s = "3456" and a = 5, s becomes "3951".
#     Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".

# Return the lexicographically smallest string you can obtain by applying the above operations any number of times on s.

# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "0158" is lexicographically smaller than "0190" because the first position they differ is at the third letter, and '5' comes before '9'.

# Example 1:
# Input: s = "5525", a = 9, b = 2
# Output: "2050"
# Explanation: We can apply the following operations:
# Start:  "5525"
# Rotate: "2555"
# Add:    "2454"
# Add:    "2353"
# Rotate: "5323"
# Add:    "5222"
# Add:    "5121"
# Rotate: "2151"
# Add:    "2050"​​​​​
# There is no way to obtain a string that is lexicographically smaller than "2050".

# Example 2:
# Input: s = "74", a = 5, b = 1
# Output: "24"
# Explanation: We can apply the following operations:
# Start:  "74"
# Rotate: "47"
# ​​​​​​​Add:    "42"
# ​​​​​​​Rotate: "24"​​​​​​​​​​​​
# There is no way to obtain a string that is lexicographically smaller than "24".

# Example 3:
# Input: s = "0011", a = 4, b = 2
# Output: "0011"
# Explanation: There are no sequence of operations that will give us a lexicographically smaller string than "0011".

# Constraints:
#     2 <= s.length <= 100
#     s.length is even.
#     s consists of digits from 0 to 9 only.
#     1 <= a <= 9
#     1 <= b <= s.length - 1

# PROBLEM SET IS SMALL ENOUGH THAT WE CAN BRUTE FORCE IT AND LOOK AT ALL PERMUTATIONS

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """Find lexicographically smallest string possible using operations A and B"""
        visited = set()
        current = set()

        current.add(s)
        visited.add(s)
    
        while current:
            next_level = set()
            
            for item in current:
                # Apply operation A
                a_value = self.a_operation(item, a)
                if a_value not in visited:
                    next_level.add(a_value)
                
                # Apply operation B
                b_value = self.b_operation(item, b)
                if b_value not in visited:
                    next_level.add(b_value)
                
            visited.update(next_level)
            current = next_level
    
        # Find lexicographically smallest string
        return min(visited)

    def a_operation(self, s: str, a: int) -> str:
        """Apply operation A: add 'a' to odd indices"""
        result = ''
        for i in range(len(s)):
            temp = int(s[i])
            if i % 2 == 0:
                result += s[i]
            else:
                calc_value = (temp + a) % 10
                result += str(calc_value)
        return result

    def b_operation(self, s: str, b: int) -> str:
        """Apply operation B: rotate string right by 'b' positions"""
        length = len(s)
        result = ''
        for i in range(length):
            result += s[(i + b) % length]
        return result


def main():
    thingy = Solution()
    print(thingy.findLexSmallestString('5525', 9, 2)) # 2050
    print(thingy.findLexSmallestString('74', 5, 1)) # 24
    print(thingy.findLexSmallestString('0011', 4, 2)) # 0011
    # print(thingy.findLexSmallestString()) # 


if __name__ == "__main__":
    main()