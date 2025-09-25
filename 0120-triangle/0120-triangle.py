class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev = triangle[0]
        minVal = prev[0]
        for row in triangle[1:]:
            temp = []
            minVal = float('inf')
            for i in range(len(row)):
                if i == 0:
                    val = prev[0] + row[i]
                elif i >= len(prev):
                    val = prev[-1] + row[i]
                else:
                    val = min(prev[i], prev[i-1]) + row[i]
                minVal = min(minVal, val)
                temp.append(val)
            prev = temp
            
        return minVal