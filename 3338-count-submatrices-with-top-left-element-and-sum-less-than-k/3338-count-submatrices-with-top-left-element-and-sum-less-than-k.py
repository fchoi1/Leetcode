class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # dp

        start = grid[0][0]
        if start > k:
            return 0

        W = len(grid[0])
        prev = [0 for _ in range(W)]
        ans = 0

        for y, row in enumerate(grid):
            curr = []
            for x, val in enumerate(row):
                currVal = val + prev[x] 
                if curr:
                    currVal += curr[-1]
                    currVal -= prev[x-1]
                
                if currVal <= k:
                    ans += 1
                curr.append(currVal)

            prev = curr
        
        return ans