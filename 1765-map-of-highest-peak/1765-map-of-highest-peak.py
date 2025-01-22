class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        H = len(isWater)
        W = len(isWater[0])
        
        def bfs(start, heights):
            q = start
            steps = 0
            seen = set()
            while q:
                temp = []
                for curr in q:
                    x,y = curr

                    if curr in seen:
                        continue
                    seen.add(curr)

                    heights[y][x] = steps
                    for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                        newX = x + dx
                        newY = y + dy
                        if W > newX >= 0 and H > newY >= 0:
                            temp.append((newX, newY))
                steps += 1
                q = temp
            return heights

        heights = []
        start = []
        for y in range(H):
            row = []
            for x in range(W):
                if isWater[y][x]:
                    row.append(0)
                    start.append((x,y))
                else:
                    row.append(-1)
            heights.append(row)      

        heights = bfs(start, heights)
        return heights