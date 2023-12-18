class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:


        transposed = [list(x) for x in zip(*matrix)]
        for i, row in enumerate(transposed):
            matrix[i] = row[::-1]
        