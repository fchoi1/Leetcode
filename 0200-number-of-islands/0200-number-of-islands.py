class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
  
      visited = {}
      m = len(grid)
      n = len(grid[0])
      #add zeros at edges
      
      for row in range(m):
        grid[row].insert(0, 0)
        grid[row].append(0)
      
      grid.insert(0, [0]*(n+2))
      grid.append([0]*(n+2))
      
      def foundIsland(row, col, grid):
        directions = [(row-1, col), (row, col-1), (row+1,col), (row,col+1)]
        for (x, y) in directions:
          if grid[x][y] == "1" and f'{x},{y}' not in visited:
            visited[f'{x},{y}'] = True
            foundIsland(x, y, grid)
        
      count = 0
      for row in range(1,m+1):
        for col in range(1,n+1):
            if grid[row][col] == "1" and f'{row},{col}' not in visited:
                foundIsland(row, col, grid)
                count += 1
      return count