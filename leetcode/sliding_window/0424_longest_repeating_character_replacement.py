# 424. Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length


import collections


# brute force solution, time complexity O(26*n^2), space complexity O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        numLettersWindow = collections.defaultdict(int)
        maxLen = 0

        for left in range(len(s)):
            numLettersWindow.clear()
            for right in range(left, len(s)):
                numLettersWindow[s[right]] += 1

                mostRepeatedLetter = ["", 0]
                for char, timesAppear in numLettersWindow.items():
                    if timesAppear > mostRepeatedLetter[1]:
                        mostRepeatedLetter = [char, timesAppear]

                lettersToChangeMakeWindowValid = (
                    right - left + 1
                ) - mostRepeatedLetter[1]
                if lettersToChangeMakeWindowValid <= k:
                    maxLen = max(maxLen, right - left + 1)

        return maxLen


# sliding window solution, time complexity O(26*n), space complexity O(n)
class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        numLettersWindow = collections.defaultdict(int)
        maxLen = 0

        left = 0
        for right in range(len(s)):
            numLettersWindow[s[right]] += 1

            numOfMostRepeatedChar = 0
            for appearances in numLettersWindow.values():
                numOfMostRepeatedChar = max(numOfMostRepeatedChar, appearances)

            windowSize = right - left + 1
            lettersToChangeMakeWindowValid = windowSize - numOfMostRepeatedChar

            if lettersToChangeMakeWindowValid <= k:
                maxLen = max(maxLen, windowSize)
            else:
                numLettersWindow[s[left]] -= 1
                left += 1

        return maxLen


# sliding window solution, time complexity O(n), space complexity O(n)
# if numOfMostRepeatedChar gets lower we can't make windowSize - numOfMostRepeatedChar <= k, because window size would grow, but  numOfMostRepeatedChar
# would stay the same or lower so maxLen is not updated, but if it's incremented, than there is a chance for it to have a maxLen
# so we just really change maxLen if numOfMostRepeatedChar gets bigger, so we just have to update it in this case
class Solution3:
    def characterReplacement(self, s: str, k: int) -> int:
        numLettersWindow = collections.defaultdict(int)
        maxLen = 0

        numOfMostRepeatedChar = 0
        left = 0
        for right in range(len(s)):
            numLettersWindow[s[right]] += 1

            numOfMostRepeatedChar = max(
                numOfMostRepeatedChar, numLettersWindow[s[right]]
            )

            windowSize = right - left + 1
            lettersToChangeMakeWindowValid = windowSize - numOfMostRepeatedChar

            if lettersToChangeMakeWindowValid <= k:
                maxLen = max(maxLen, windowSize)
            else:
                numLettersWindow[s[left]] -= 1
                left += 1

        return maxLen
