class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMap = {}
        used = set()
        if len(s) != len(s):
            return False

        for a,b in zip(s,t):
            if a in charMap and charMap[a] != b:
                return False
            if b in used and (a not in charMap or charMap[a] != b):
                return False
            charMap[a] = b
            used.add(b)
        return True

        