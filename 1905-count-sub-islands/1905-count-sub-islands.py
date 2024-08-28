class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def count_island(node, island):
            if node in island:
                return True
            x,y = node
            island.add(node)
            isSub = True
            for dx, dy in [(0,1), (1,0), (-1,0), (0, -1)]:
                if 0 <= x + dx < W and 0 <= y + dy < H:
                    if grid2[y + dy][x + dx]:
                        if not count_island((x + dx, y + dy), island):
                            isSub = False
            return isSub and grid1[y][x]

        
        H = len(grid1)
        W = len(grid1[0])
        island = set()
        count = 0

        for y in range(H):
            for x in range(W):
                if grid2[y][x] and (x,y) not in island:
                    isSub = count_island((x,y), island)
                    if isSub:
                        count += 1 
                    # print(island, count, bool(isSub), x,y)
        print(island, count)
        return count

