class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        translate = {}
        for sChar, tChar in zip(s,t):
            if sChar in translate and translate[sChar] != tChar:
                return False
            if sChar not in translate:
                
                translate[sChar] = tChar
                if ':' + tChar in translate:
                    return False
                translate[':'+tChar] = sChar
        return True
        