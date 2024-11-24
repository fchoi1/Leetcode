class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minVal = abs(matrix[0][0])
        currSum = c = 0
        hasZero = False
        for row in matrix:
            for val in row:
                if val < 0:
                    c += 1
                if val == 0:
                    hasZero = True
                minVal = min(minVal, abs(val))
                currSum += abs(val)
        if c % 2 == 1 and not hasZero:
            return currSum - 2 * minVal
        return currSum