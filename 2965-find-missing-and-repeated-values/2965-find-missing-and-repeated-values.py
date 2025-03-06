class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        N = len(grid)
        maxVal = N * N
        curr = 0
        total =  maxVal * (maxVal + 1) // 2
        seen = set()
      
        for row in grid:
            for val in row:
                total -= val
                if val in seen:
                    dupe = val
                seen.add(val)

        return [dupe, dupe + total]
        