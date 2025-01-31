class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        letterMap = {}
        used = set()

        for a,b in zip(s,t):
            if a in letterMap:
                if letterMap[a] != b:
                    return False
            elif b in used:
                return  False
            else:
                used.add(b)
                letterMap[a] = b
        return True
        