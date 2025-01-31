class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        W = len(matrix[0])
        H = len(matrix)

        for i in range(W):
            start = matrix[0][i]
            x,y = i,0
            while W > x >= 0 and H > y >= 0:
                print(x,y, matrix[y][x])
                if matrix[y][x] != start:
                    return False
                y += 1
                x += 1

        for j in range(H):
            start = matrix[j][0]
            x,y = 0,j
            while W > x >= 0 and H > y >= 0:
                if matrix[y][x] != start:
                    return False
                y += 1
                x += 1
        
        return True
        