class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = []
        ans = sum(matrix[0])
        for y in range(1, m):
            ans += matrix[y][0]
            for x in range(1, n):
                if matrix[y][x]:
                    matrix[y][x] += min(matrix[y - 1][x], matrix[y][x - 1], matrix[y- 1][x - 1])
                    ans += matrix[y][x]
            
        return ans
