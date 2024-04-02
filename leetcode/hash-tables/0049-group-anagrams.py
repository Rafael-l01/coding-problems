# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


from collections import defaultdict
from typing import List


# my first solution
class Solution1:
    def builtStrMap(self, s: str):
        mapS = {}
        for i in range(len(s)):
            if s[i] in mapS:
                mapS[s[i]] += 1
            else:
                mapS[s[i]] = 1

        return mapS

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        anagramsWithMap = []
        for str in strs:
            wasAdded = False
            strMap = self.builtStrMap(str)

            for i, group in enumerate(anagramsWithMap):
                if len(group[0]["s"]) == len(str):
                    if group[0]["map"] == strMap:
                        anagrams[i].append(str)
                        wasAdded = True
                        break
                else:
                    continue

            if not wasAdded:
                anagramsWithMap.append([{"s": str, "map": strMap}])
                anagrams.append([str])

        return anagrams


# second solution with O(n*m) time complexity with n as the number of strings and m the avg number of chars in each
class Solution:
    def groupAnagrams(self, strs):
        anagramGroups = defaultdict(list)

        for str in strs:
            charCount = [0] * 26

            for char in str:
                charCount[ord(char) - ord("a")] += 1

            anagramGroups[tuple(charCount)].append(str)

        return anagramGroups.values()
