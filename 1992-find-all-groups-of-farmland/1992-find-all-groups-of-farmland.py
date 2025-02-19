class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        W = len(land[0])
        H = len(land)

        def search(x,y):
            while y < H and land[y][x]:
                y += 1
            y -= 1
            while x < W and land[y][x]:
                x += 1
            x -= 1
            return x,y
            
        # left up corners
       
        groups = []
        for y in range(H):
            for x in range(W):
                if not land[y][x]:
                    continue
                isLeftCorner = (
                    (x == 0 and y == 0 and land[y][x]) or
                    (x == 0 and not land[y-1][x]) or
                    (y == 0 and not land[y][x-1]) or
                    (not land[y][x-1] and not land[y-1][x])
                )
                if isLeftCorner:
                    nx, ny = search(x,y)
                    groups.append((y,x,ny,nx))

        return groups