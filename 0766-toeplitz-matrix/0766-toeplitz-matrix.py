class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        W = len(matrix[0])
        H = len(matrix)
        def checkDiag(pos):
            x, y = pos
            val = matrix[y][x]
            while 0 <= x < W and 0 <= y < H:
                if val != matrix[y][x]:
                    return False
                x,y = x + 1, y + 1
            return True
                
        # first col
        for i in range(H):
            if not checkDiag((0,i)):
                return False

        # first row
        for i in range(W):
            if not checkDiag((i,0)):
                return False
        return True
            
        