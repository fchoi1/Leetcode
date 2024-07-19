class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        maxN = set()
        minN = set()
        for row in matrix:
            minN.add(min(row))
        
        for i in range(len(matrix[0])):
            maxN.add(max(x[i] for x in matrix))
            
        return maxN.intersection(minN)