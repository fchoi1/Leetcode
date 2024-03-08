class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        ptr = 0
        for char in t:
            if char == s[ptr]:
                ptr += 1
            if ptr >= len(s):
                return True
        return False
        