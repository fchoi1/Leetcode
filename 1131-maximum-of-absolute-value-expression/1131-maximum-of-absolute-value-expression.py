class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        


        # (x1 - y1) + (x2 - y2) = i - j 
        # (y1 - x1) + (x2 - y2) = i - j
        # (y1 - x1) + (y2 - x2) = i - j
        # (x1 - y1) + (y2 - x2) = i - j

        # f(i) = a(x_i) +b(y_i) for a = [1,-1,1,-1] and b = [1,1,-1,-1]
        # f(i) - f(j) -> get this maxVal
        maxVal = 0
        for a,b in [[1,1],[-1,1],[1,-1],[-1,-1]]:
            smallest = a * arr1[0] + b * arr2[0] 
            for i,(x,y) in enumerate(zip(arr1, arr2)):
                curr = a * x + b * y + i
                maxVal = max(maxVal, abs(curr-smallest))
                smallest = min(smallest, curr)
        return maxVal


