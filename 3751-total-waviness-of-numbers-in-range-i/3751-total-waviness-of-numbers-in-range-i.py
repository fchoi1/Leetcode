class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for n in range(max(100,num1), num2 + 1):
            s = str(n)
            length = len(s)
            counts = 0
            for i in range(1, length - 1):
                if s[i - 1] < s[i] > s[i + 1] or s[i - 1] > s[i] < s[i + 1]:
                    counts += 1
            ans += counts
    
        return ans