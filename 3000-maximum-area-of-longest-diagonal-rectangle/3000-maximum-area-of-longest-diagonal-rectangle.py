class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag = maxArea = 0
        for w, l in dimensions:
            currDiag = math.sqrt(w*w + l*l) 
            if currDiag > diag:
                maxArea = w*l 
                diag = currDiag 
            elif diag == currDiag:
                maxArea = max(maxArea, w*l )
        return maxArea