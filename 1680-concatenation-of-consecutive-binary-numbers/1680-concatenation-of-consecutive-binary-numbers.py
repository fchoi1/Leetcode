class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        for i in range(1,n + 1):
            l = len(bin(i)) - 2
            ans <<= l 
            ans += i
            ans %= (10 ** 9 + 7)
        return ans
