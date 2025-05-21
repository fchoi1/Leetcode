class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # get all zeros

        cols = set()
        rows = set()
        for y, row in enumerate(matrix):
            for x, val in enumerate(row):
                if val == 0:
                    cols.add(x)
                    rows.add(y)
        
        for y, row in enumerate(matrix):
            for x  in range(len(row)):
                if y in rows or x in cols:
                    matrix[y][x] = 0
        