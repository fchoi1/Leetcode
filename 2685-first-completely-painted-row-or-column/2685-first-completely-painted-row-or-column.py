class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:


        H = len(mat)
        W = len(mat[0])

        rows = [0] * H
        cols = [0] * W

        coords = {}
        for y in range(H):
            for x in range(W):
                coords[mat[y][x]] = (x,y)

        for i, n in enumerate(arr):
            x,y = coords[n]
            rows[y] += 1
            cols[x] += 1
            if rows[y] >= W or cols[x] >= H:
                return i
        return -1

        

            
        