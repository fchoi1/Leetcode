class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        N = len(s)
        if N == 1:
            return s

        def getPali(l,r):
            if s[l] != s[r]:
                return (l,r)

            while s[l] == s[r] and r < N - 1 and l > 0:
                l -= 1 
                r += 1
                if s[l] != s[r]:
                    l += 1
                    r -= 1
                    break

            return (l, r + 1)

        longest = 0
        ans = ''
        for i in range(N):

            l_odd,r_odd = getPali(i, i) 
            if i > 0:
                l_even,r_even = getPali(i, i-1) 
                if r_even - l_even > longest:
                    longest = r_even - l_even
                    ans = s[l_even:r_even]
                
                
            if r_odd - l_odd > longest:
                longest = r_odd - l_odd
                ans = s[l_odd:r_odd]

        return ans 