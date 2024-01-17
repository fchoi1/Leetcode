class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
  
      visited = set()
      m = len(grid)
      n = len(grid[0])
      
      def inRange(x,y):
          return 0 <= x < m and 0 <= y < n

      def foundIsland(row, col, grid):
        directions = [(row-1, col), (row, col-1), (row+1,col), (row,col+1)]
        for (x, y) in directions:
          if inRange(x,y) and grid[x][y] == "1" and (x,y) not in visited:
                visited.add((x,y))
                foundIsland(x, y, grid)
        
      count = 0
      for row in range(m):
        for col in range(n):
            if grid[row][col] == "1" and (row,col) not in visited:
                foundIsland(row, col, grid)
                count += 1
      return count