class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        
        arr = []
        for row in grid:
            arr.extend(row)
        
        n = len(arr)
        
        prefix = [1] * n
        suffix = [1] * n
        
        for i in range(1, n):
            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD
        
        for i in range(n-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
        
        res = []
        idx = 0
        
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                row.append((prefix[idx] * suffix[idx]) % MOD)
                idx += 1
            res.append(row)
        
        return res