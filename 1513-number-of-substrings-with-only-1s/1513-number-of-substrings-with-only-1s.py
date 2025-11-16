class Solution:
    def numSub(self, s: str) -> int:
        
        ones = 0 
        mod = 10 ** 9 + 7
        ans = 0
        for char in s:
            if char == '1':
                ones += 1
            else:
                ones = 0
            ans = (ans + ones) % mod
        
        return ans % mod