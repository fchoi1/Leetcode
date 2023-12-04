class Solution:
    def largestGoodInteger(self, num: str) -> str:
        digit = -1
        for i,c in enumerate(num[:-2]):
            if all(x == c for x in num[i:i+3]):
                digit = max(digit,int(c))
        return str(digit)*3 if digit != -1 else ""