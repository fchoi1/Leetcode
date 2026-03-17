class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # largest rectangle 
        # interval check

        # x 0 x
        # x 0 0 
        # x x 0

        # group by row first,
        # check cols
        W = len(matrix[0])
        H = len(matrix)

        cumulative = [0 for _ in range(W)]
        largest = 0
        for row in matrix:
            for i,x in enumerate(row):
                if x:
                    cumulative[i] += 1
                else:
                    cumulative[i] = 0

            curr = 0
            for idx, val in enumerate(sorted(cumulative)):
                if val == 0:
                    continue
                largest = max(largest, val * (W - idx))

        return largest
            
