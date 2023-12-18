class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
 
        for j, row in enumerate(matrix):
            for i in range(j,len(row)):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

        for i, row in enumerate(matrix):
            matrix[i] = row[::-1]
        