class Solution:
    def maxOperations(self, s: str) -> int:
        # max start from left? # add

        ones = 0 
        zeros = 0
        ans = 0
        N = len(s)
        for i, char in enumerate(s):

            if char == '0':
                zeros += 1
                

            if char == '1':
                ones += 1

                if i == N - 1:
                    break
                if s[i + 1] == '0':
                    ans += ones
                
                zeros = 0

        return ans
                

            