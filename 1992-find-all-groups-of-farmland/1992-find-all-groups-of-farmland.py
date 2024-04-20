class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        farmland = []

        H = len(land)
        W = len(land[0])

        def traverse(x,y,botX, botY):
            if x < 0 or x >= W or y < 0 or y >= H or not land[y][x]:
                return (botX, botY)

            land[y][x] = 0 
            botX, botY = max(botX, x),max(botY, y)

            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                botX, botY = traverse(x+dx,y+dy, botX, botY)
            return (botX, botY)


        for y in range(H):
            for x in range(W):
                if land[y][x]:
                    botX, botY = traverse(x,y,x,y)
                    farmland.append([y,x,botY,botX])

        return farmland
        