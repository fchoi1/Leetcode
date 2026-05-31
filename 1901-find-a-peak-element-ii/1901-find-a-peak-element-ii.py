class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        # find any peak in m log n

        # split in 2 halfs

        # pick one square and keep going up?

        curr = (0,0)

        W = len(mat[0])
        H = len(mat)

        def check(x,y):
            
            curr = mat[y][x]
            best = (None, None) # val, coord
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < W and 0 <= ny < H:
                    if mat[ny][nx] > curr:
                        if best[0] is None:
                            best = (mat[ny][nx], (nx, ny))
                        else:
                            best = max(best, (mat[ny][nx], (nx, ny)))
            return best


        best = (mat[0][0], (0,0))
        while best[0] is not None:

            best = check(curr[0], curr[1])

            if best[0] is None:
                return (curr[1], curr[0])
            
            curr = best[1]

        return -1
