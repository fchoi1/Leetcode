class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        stringSet = set()
        
        for a,b in zip(s, s[1:]):
            stringSet.add(a+b)
        reversedS = s[::-1]
        for a,b in zip(reversedS, reversedS[1:]):
            if a+b in stringSet:
                return True
        return False
        
        
        