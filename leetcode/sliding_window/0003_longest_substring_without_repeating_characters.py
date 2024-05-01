# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


# time complexity O(n), space complexity O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowLetters = set()
        maxLen = 0

        left, right = 0, 0
        while right < len(s):
            if s[right] in windowLetters:
                maxLen = max(maxLen, right - left)
                while s[left] != s[right]:
                    windowLetters.remove(s[left])
                    left += 1
                left += 1
            else:
                windowLetters.add(s[right])

            right += 1

        maxLen = max(maxLen, right - left)
        return maxLen


# better solution
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowLetters = set()
        maxLen = 0

        left = 0
        for right in range(len(s)):
            while s[right] in windowLetters:
                windowLetters.remove(s[left])
                left += 1

            windowLetters.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen
