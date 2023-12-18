class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
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