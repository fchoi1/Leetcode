class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # dfs 
        cache = {}
        N = len(triangle)

        # get min, sum at node
        def dfs(index, row):
            if (index, row) in cache:
               return cache[(index,row)]

            if row < N:
                left = dfs(index, row + 1)
                right = dfs(index + 1, row + 1)
                
                cache[(index, row)] = triangle[row][index] + min(left, right)
                return cache[(index, row)]
            else:
                return 0

    
        
        dfs(0,0)
        return cache[(0,0)]