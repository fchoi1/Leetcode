from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        start = 0
        num = 0
        denom = 1
        N = len(expression) 
        for i,char in enumerate(expression + "+"):
            if (char in "+-" or i == N) and i != 0:
                top = int(expression[start:i].split("/")[0])
                bot = int(expression[start:i].split("/")[1])
                num = num * bot + denom * top
                denom *= bot
                start = i 
        if num == 0:
            return "0/1"
        factor = gcd(num, denom)
        return f"{num//factor}/{denom//factor}"
        