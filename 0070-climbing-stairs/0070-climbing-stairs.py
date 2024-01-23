class Solution:
    def climbStairs(self, n: int) -> int:
        steps = []

        for i in range(n):
            if i in [0, 1]:
                steps.append(i + 1)
                continue
            steps.append(steps[i-1] +  steps[i-2])
        return steps[-1]
