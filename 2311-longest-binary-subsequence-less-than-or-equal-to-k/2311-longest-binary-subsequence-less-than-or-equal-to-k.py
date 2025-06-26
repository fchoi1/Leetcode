class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # dp / greedy
        # 101

        longest = s.count('0')
        currStr = ''
        for b in s[::-1]:
            if b == '0':
                currStr = b + currStr
            else:
                if int(b + currStr,2) <= k:
                    currStr = b + currStr




        return len(currStr)