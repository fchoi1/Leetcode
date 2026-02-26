class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0

        while int(s,2) != 1:
            n = int(s,2)
            if n % 2 == 0:
                s = bin(n//2)[2:]
            else:
                s = bin(n + 1)[2:]
            steps += 1
            
        return steps