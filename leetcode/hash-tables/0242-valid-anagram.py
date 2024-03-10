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
