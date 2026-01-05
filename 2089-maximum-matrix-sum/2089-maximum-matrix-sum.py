class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        currSum = 0
        neg = 0
        smallest = inf
        for row in matrix:
            for val in row:
                currSum += abs(val)
                smallest = min(smallest, abs(val))
                if val <= 0:
                    neg += 1

        if neg % 2 == 0:
            return currSum
        return currSum - 2 * smallest
       
