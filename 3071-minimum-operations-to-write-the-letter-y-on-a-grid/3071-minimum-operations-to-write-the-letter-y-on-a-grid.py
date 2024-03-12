class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        half = n//2
        def check(yVal, notYVal):
            steps = 0
            for y in range(n):
                for x in range(n):
                    if (y >= n // 2 and x == n//2) or (y < n // 2 and (x == y or y == n - x - 1)):
                        if grid[y][x] != yVal:
                            steps += 1
                    elif grid[y][x] != notYVal:
                        steps += 1
            return steps
        minSteps = inf
        for yVal, notYVal in [[0,1],[1,0],[1,2],[2,1],[0,2],[2,0]]:
            minSteps = min(minSteps, check(yVal, notYVal))
        return minSteps
