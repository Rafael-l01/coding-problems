# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            mapS = {}
            mapT = {}

            for i in range(len(s)):
                if s[i] in mapS:
                    mapS[s[i]] += 1
                else:
                    mapS[s[i]] = 1

                if t[i] in mapT:
                    mapT[t[i]] += 1
                else:
                    mapT[t[i]] = 1

            if mapS == mapT:
                return True

        return False


# time complexity O(n), space complexity O(n)
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            mapS = collections.defaultdict(int)
            mapT = collections.defaultdict(int)

            for i in range(len(s)):
                mapS[s[i]] += 1
                mapT[t[i]] += 1

            return mapS == mapT

        return False
