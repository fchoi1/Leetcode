class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        longest = 0
        zeros = start = ones = 0

        for i, val in enumerate(s):
            if val == '0':
                if i > 0 and s[i-1] == '1':
                    zeros = 0
                if not zeros:
                    start = i
                zeros += 1
                ones = 0
            else:
                print(zeros, ones, longest)
                if not zeros:
                    continue
                else:
                    zeros -= 1
                    ones += 1
                    longest = max(longest,  ones * 2)

        return longest
        