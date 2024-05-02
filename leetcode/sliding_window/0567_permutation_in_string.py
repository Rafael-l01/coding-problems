# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


import collections


# time complexity O(26*n + m), space complexity O(52) -> considering n the size of s2 and m the size of s1
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        numCharS1 = [0] * 26
        for char in s1:
            numCharS1[ord(char) - ord("a")] += 1

        left = 0
        numCharWindow = [0] * 26
        for right in range(len(s2)):
            numCharWindow[ord(s2[right]) - ord("a")] += 1

            if (right - left + 1) == len(s1):
                if numCharS1 == numCharWindow:
                    return True

                numCharWindow[ord(s2[left]) - ord("a")] -= 1
                left += 1

        return False


# time complexity O(26*n), space complexity O(52) -> considering n the size of s2 and m the size of s1
class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        numCharS1 = collections.defaultdict(int)
        for char in s1:
            numCharS1[char] += 1

        left = 0
        numCharWindow = collections.defaultdict(int)
        for right in range(len(s2)):
            numCharWindow[s2[right]] += 1

            if (right - left + 1) == len(s1):
                if numCharS1 == numCharWindow:
                    return True

                numCharWindow[s2[left]] -= 1
                if numCharWindow[s2[left]] == 0:
                    del numCharWindow[s2[left]]

                left += 1

        return False
