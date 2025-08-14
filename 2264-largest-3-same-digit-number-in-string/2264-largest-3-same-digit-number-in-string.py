class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ''
        for a,b,c in zip(num, num[1:], num[2:]):
            if a == b == c:
                ans = max(ans, a * 3)
        

        return ans