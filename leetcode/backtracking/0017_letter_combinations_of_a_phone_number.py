# 17. Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]


# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

from typing import List


# time complexity O(n * (4^n)), space complexity O((4^n) + n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        allComb = []
        mapDigitToLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, comb):
            if len(comb) == len(digits):
                if len(comb) > 0:
                    string = ""
                    for char in comb:
                        string += char

                    allComb.append(string)
                return

            for letter in mapDigitToLetter[digits[i]]:
                comb.append(letter)
                backtrack(i + 1, comb)

                comb.pop()

        backtrack(0, [])
        return allComb


# time complexity O(n * (4^n)), space complexity O((4^n) + n)
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        allComb = []
        mapDigitToLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, comb):
            if len(comb) == len(digits):
                allComb.append(comb)
                return

            for letter in mapDigitToLetter[digits[i]]:
                backtrack(i + 1, comb + letter)

        if len(digits) > 0:
            backtrack(0, "")

        return allComb
