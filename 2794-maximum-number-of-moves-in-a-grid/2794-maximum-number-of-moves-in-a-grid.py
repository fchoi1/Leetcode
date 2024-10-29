class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # cache
        N = len(grid[0])
        M = len(grid)
        cache = {}
        
        def dfs(x,y):        
            if x >= N - 1:
                cache[(x,y)] = 1
                return 1
    
            if (x,y) in cache:
                return cache[(x,y)] 

            s = 0
            for i in [-1, 0, 1]:
                if 0 <= y + i < M: 
                    if (x + 1 < N and grid[y][x] < grid[y + i][x + 1]):
                        s = max(s, dfs(x + 1, y + i))
   
            cache[(x,y)] = s + 1
            return s  + 1

        col = len(grid)
        ans = 0
        for i in range(col):
            ans = max(ans, dfs(0, i))
        return max(ans - 1, 0)

            
        