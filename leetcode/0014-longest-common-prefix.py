# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


from typing import List


# first solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstString = strs[0]
        longestPrefix = firstString

        for i in range(1, len(strs)):
            str2 = strs[i]
            longestP2 = ""
            for j, char in enumerate(firstString):
                if j < len(str2) and char == str2[j]:
                    longestP2 += char
                else:
                    break

            longestPrefix = min(longestPrefix, longestP2)

        return longestPrefix


# second solution
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = ""

        for i in range(len(strs)):
            charCompare = 0
            actualString = strs[i]
            while charCompare < len(longestPrefix) and charCompare < len(actualString):
                if longestPrefix[charCompare] == actualString[charCompare]:
                    charCompare += 1
                else:
                    break

            longestPrefix = longestPrefix[0:charCompare]

        return longestPrefix


# third solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = ""

        for i in range(len(strs[0])):
            for str in strs:
                if i == len(str) or str[i] != strs[0][i]:
                    return longestPrefix

            longestPrefix += strs[0][i]

        return longestPrefix
