class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def inBounds(x,y):
            return 0<= x < W and 0<=y<H
        transpose = [list(x) for x in zip(*mat)]
        W = len(mat[0])
        H = len(mat)
        diags = [[] for _ in range(H+W -1)]
        for j in range(H):
            for i in range(W):
                s = i + j
                diags[s].append(mat[j][i])
        res = []
        i = -1
        for row in diags:
            res.extend(row[::i])
            i*=-1
        return res