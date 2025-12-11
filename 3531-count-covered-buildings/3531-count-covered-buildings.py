class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        
        rows = defaultdict(list)
        cols = defaultdict(list)
        for x,y in buildings:
            
            if len(rows[x]) == 0:
                rows[x] = [y,y]
            else:
                rows[x] = [min(rows[x][0], y), max(rows[x][1], y)]

            if len(cols[y]) == 0:
                cols[y] = [x,x]
            else:
                cols[y] = [min(cols[y][0], x), max(cols[y][1], x)]
        
        
        count = 0
        for x,y in buildings:
            if rows[x][0] < y < rows[x][1] and cols[y][0] < x < cols[y][1]:
                count += 1

        return count