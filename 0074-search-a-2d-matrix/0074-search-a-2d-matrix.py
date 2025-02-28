class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      
      m = len(matrix)
      n = len(matrix[0])
            
      currIndex = counter =  m * n // 2
            
      def getRowCol(n: int , index: int ):
        row = index // n
        col = index % n
        return (row, col)
      start = 0
      end = m*n

      while end > start:
        mid = (end + start) // 2
        
        (currRow, currCol) = getRowCol(n, mid)
        if matrix[currRow][currCol] == target:
          return True
        elif matrix[currRow][currCol] < target:
          start = mid + 1 
        else:
          end = mid
      return False
    
