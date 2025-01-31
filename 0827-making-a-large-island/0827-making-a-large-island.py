class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def dfs(node, groupId, seen):
            x,y = node
            if grid[y][x] < 1:
                return seen

            grid[y][x] = groupId
            seen.add((x,y))
            
            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                newX, newY = x + dx, y + dy
                nextNode = (newX, newY) 
                if N > newX >= 0 and N > newY >= 0 and nextNode not in seen and grid[newY][newX] > 0:
                    seen = dfs(nextNode, groupId, seen)
            return seen



        self.sizes = {}
        groupId = -1
        largest = 0
        for y in range(N):
            for x in range(N):
                if grid[y][x] < 1:
                    continue
                g = dfs((x,y), groupId, set())
                self.sizes[groupId] = len(g)
                largest = max(largest, len(g))
                groupId -= 1

        print(grid)
        print(self.sizes)

        for y in range(N):
            for x in range(N):
                if grid[y][x] != 0:
                    continue

                currSize = 1
                seenGroup = set()
                for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                    newX, newY = x + dx, y + dy
                    node = (newX, newY)

                    if N > newX >= 0 and N > newY >= 0 and grid[newY][newX] < 0:
                        gid = grid[newY][newX] 
                        if gid in seenGroup:
                            continue
                        seenGroup.add(gid)
                        currSize += self.sizes[gid]
                largest = max(largest, currSize)

        return largest

                