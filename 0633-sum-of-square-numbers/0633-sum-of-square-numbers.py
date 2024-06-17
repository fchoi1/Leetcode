class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(math.sqrt(c))

        while a <= b:
            square = a * a + b * b
            print(a,b, square)
            if square == c:
                return True
            if square < c:
                 a += 1
            else:
                b -= 1
            
        # c = 1-
        return False