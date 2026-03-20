class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # track min and max
        W = len(grid[0])
        H = len(grid)

        W_k = W - k + 1
        H_k = H - k + 1

        ans = [[0 for _ in range(W_k)] for _ in range(H_k)]

        for y in range(H_k):
            for x in range(W_k):
                curr = set()
                for j in range(y, y + k):
                    for i in range(x, x + k):
                        curr.add(grid[j][i])     
                        
                sorted_curr = sorted(curr)
                if len(curr) > 1:
                    ans[y][x] = min(abs(p-c) for p,c in zip(sorted_curr, sorted_curr[1:]))

        return ans