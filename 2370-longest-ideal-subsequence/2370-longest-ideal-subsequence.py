class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for char in s:
            maxLen = 1
            index = ord(char)-ord('a') 
            for i in range(max(0, index - k), min(26, index + k + 1)):
                maxLen = max(maxLen, dp[i] + 1 )
            dp[ord(char)-ord('a')] = maxLen
        return max(dp)