class Solution:
    def numSteps(self, s: str) -> int:
        # 1110
        # 111
        # 1000
        # 100
        # 10
        # 1
        steps = 0
        n = int(s,2)
        while n != 1:
            if n % 2 == 1:
                n += 1
            else:
                n >>= 1
            steps += 1
        return steps

        
        