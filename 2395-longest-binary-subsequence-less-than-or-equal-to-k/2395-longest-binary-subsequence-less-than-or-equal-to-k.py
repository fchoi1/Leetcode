class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:

        currStr = ''
        for b in s[::-1]:
            if b == '0':
                currStr = b + currStr
            else:
                if int(b + currStr,2) <= k:
                    currStr = b + currStr

        return len(currStr)