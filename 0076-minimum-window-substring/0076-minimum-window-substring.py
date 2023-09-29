from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        minStr = ''
        minLength = float('inf')
        tDict = Counter(t)
        sDict = Counter()

        for right, char in enumerate(s):
            if char in tDict:
                sDict[char] += 1
            
            while all(sDict[char] >= tDict[char] for char in tDict):
                if right - left < minLength:
                    minLength = right - left 
                    minStr = s[left:right+1]
                if s[left] in sDict:
                    sDict[s[left]] -= 1
                left += 1
        return minStr