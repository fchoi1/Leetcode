class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            return isPali(l, r-1) or isPali(l+1, r)
        return True
        
    
        