# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.


# using built-in functions
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for char in s:
            if char.isalnum():
                newS += char.lower()

        reversedS = ""
        for i in range(len(newS) - 1, -1, -1):
            reversedS += newS[i]

        if newS == reversedS:
            return True

        return False


# using two pointers technique
class Solution:
    def isAlphaNum(self, char):
        if ord(char) >= ord("0") and ord(char) <= ord("9"):
            return True
        if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            return True
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            return True

        return False

    def isPalindrome(self, s: str) -> bool:
        firstPointer = 0
        secondPointer = len(s) - 1

        while firstPointer < secondPointer:
            while firstPointer < secondPointer and not self.isAlphaNum(s[firstPointer]):
                firstPointer += 1

            while secondPointer > firstPointer and not self.isAlphaNum(
                s[secondPointer]
            ):
                secondPointer -= 1

            if not s[firstPointer].lower() == s[secondPointer].lower():
                return False

            firstPointer += 1
            secondPointer -= 1

        return True


# two pointer without lower built-in function
class Solution:
    def isAlphaNum(self, char):
        if ord(char) >= ord("0") and ord(char) <= ord("9"):
            return True
        if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            return True
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            return True

        return False

    def isAlpha(self, char):
        if ord(char) >= ord("A") and ord(char) <= ord("Z"):
            return True
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            return True

        return False

    def isSameAlphaNum(self, a, b):
        if a == b:
            return True

        if self.isAlpha(a) and self.isAlpha(b):
            if ord(a) - 32 == ord(b) or ord(a) + 32 == ord(b):
                return True

        return False

    def isPalindrome(self, s: str) -> bool:
        firstPointer = 0
        secondPointer = len(s) - 1

        while firstPointer < secondPointer:
            while firstPointer < secondPointer and not self.isAlphaNum(s[firstPointer]):
                firstPointer += 1

            while secondPointer > firstPointer and not self.isAlphaNum(
                s[secondPointer]
            ):
                secondPointer -= 1

            if not self.isSameAlphaNum(s[firstPointer], s[secondPointer]):
                return False

            firstPointer += 1
            secondPointer -= 1

        return True
