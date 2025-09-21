from typing import List

# Horrid description what it breaks into is:
# check these in order
# exact match --- return it
# case-insensitive match -- return matching word (via lowercase)
# vowel match -- take list lowercase it and return all words with * for the vowel
# (Check the subroutine)
# Otherwise return an empty string
#
# Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.
# For a given query word, the spell checker handles two categories of spelling mistakes:
#     Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
#         Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
#         Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
#         Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
#     Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
#         Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
#         Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
#         Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
#
# In addition, the spell checker operates under the following precedence rules:
#     When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
#     When the query matches a word up to capitlization, you should return the first such match in the wordlist.
#     When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
#     If the query has no matches in the wordlist, you should return the empty string.
#
# Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].
#
# Example 1:
# Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
#
# Example 2:
# Input: wordlist = ["yellow"], queries = ["YellOw"]
# Output: ["yellow"]
#
# Constraints:
#
#     1 <= wordlist.length, queries.length <= 5000
#     1 <= wordlist[i].length, queries[i].length <= 7
#     wordlist[i] and queries[i] consist only of only English letters.

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exactMatch = set(wordlist)
        caseInsensitive = {}
        vowelMatch = {}

        for word in wordlist:
            caseInsensitive.setdefault(word.lower(), word)
            vowelMatch.setdefault(self.__vowelMask(word), word)

        # print(exactMatch)
        # print(caseInsensitive)
        # print(vowelMatch)

        retVal: List[str] = []
        for query in queries:
            if query in exactMatch:
                retVal.append(query)
            elif query.lower() in caseInsensitive:
                retVal.append(caseInsensitive[query.lower()])
            else:
                temp: str = self.__vowelMask(query)
                if temp in vowelMatch:
                    retVal.append(vowelMatch[temp])
                else:
                    retVal.append("")

        return retVal

    def __vowelMask(self, word: str) -> str:
        temp = word.lower()
        temp = temp.replace("a", "*")
        temp = temp.replace("e", "*")
        temp = temp.replace("i", "*")
        temp = temp.replace("o", "*")
        temp = temp.replace("u", "*")
        return temp

def main():
    thingy = Solution()

    # ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
    print(thingy.spellchecker(["KiTe","kite","hare","Hare"],["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]))
    print(thingy.spellchecker(["yellow"], ["YellOw"])) # ["yellow"]

if __name__ == "__main__":
    main()          