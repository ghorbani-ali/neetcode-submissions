class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        aS = {}
        aT = {}
        for i in range(len(s)):
            if aS.get(s[i]) == None:
                aS[s[i]] = 1
            else:
                aS[s[i]] += 1
            if aT.get(t[i]) == None:
                aT[t[i]] = 1
            else:
                aT[t[i]] += 1
        
        if aS != aT:
            return False

        return True