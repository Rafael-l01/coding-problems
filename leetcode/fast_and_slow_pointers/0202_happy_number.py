# 202. Happy Number

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false


# Constraints:

# 1 <= n <= 231 - 1


# first solution, time complexity is O(n^2), and space complexity is O(n)
# using a set is time complexity O(n)
class Solution:
    def isHappy(self, n: int) -> bool:
        nStr = str(n)
        numbers = []
        while True:
            nextN = 0
            for char in nStr:
                nextN += int(char) ** 2

            if nextN in numbers:
                return False

            if nextN == 1:
                return True

            numbers.append(nextN)
            nStr = str(nextN)


# second solution using fast and slow pointers, time complexity is O(n), considering n the number of numbers in the "list", and space complexity is O(1)
class Solution2:
    def getSumSquares(self, n):
        sumSquares = 0
        while n > 0:
            digit = n % 10
            sumSquares += digit**2
            n = n // 10

        return sumSquares

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while True:
            slow = self.getSumSquares(slow)
            fast = self.getSumSquares(self.getSumSquares(fast))

            if slow == fast:
                break

        return slow == 1
