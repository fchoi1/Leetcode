class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeros = longest = ones = 0

        for i, val in enumerate(s):
            if val == '0':
                # Reset counts if a zero appears after 1
                if i > 0 and s[i-1] == '1':
                    zeros = 0
                    ones = 0
                zeros += 1
            else:
                ones += 1
            if ones <= zeros:
                longest = max(longest,  ones * 2)

        return longest
        