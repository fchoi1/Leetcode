class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for char in s:
            maxLen = 1
            for i in range(26):
                if abs(ord(char)-ord('a') - i) <= k:
                    maxLen = max(maxLen, dp[i] + 1 )
            dp[ord(char)-ord('a')] = maxLen
        print(dp)
        return max(dp)