class Solution:
    def maxScore(self, s: str) -> int:
        total = len(s)
        ones = s.count('1')
        zeros = 0
        ans = 0
        
        for char in s[:-1]:
            if char == '0':
                zeros += 1
            else:
                ones -= 1
            ans = max(ans, zeros + ones)
        return ans 
