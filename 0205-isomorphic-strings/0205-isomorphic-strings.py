class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        letterMap = {}
        used = set()

        for a,b in zip(s,t):
            if a in letterMap and letterMap[a] == b:
                continue
            if b in used or (a in letterMap and letterMap[a] != b):
                return  False
            used.add(b)
            letterMap[a] = b
        return True
        