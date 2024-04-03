class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeros = longest = ones = 0
        prev = None

        for val in s:
            if val == '0':
                # Reset counts if a zero appears after 1
                if prev == '1':
                    zeros = 0
                    ones = 0
                zeros += 1
            else:
                ones += 1
            if ones <= zeros:
                longest = max(longest,  ones * 2)
            prev = val

        return longest
        