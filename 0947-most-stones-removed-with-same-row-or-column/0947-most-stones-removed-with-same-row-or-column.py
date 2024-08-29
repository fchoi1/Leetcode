class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
       
        def dfs(node, seen):
            if node in seen:
                return seen
            x,y = node
            seen.add((x,y))
            for nextY in row[x]:
                seen = dfs((x,nextY), seen)
            
            for nextX in col[y]:
                seen = dfs((nextX,y), seen)
            return seen

        row = defaultdict(list)
        col = defaultdict(list)
        for x,y in stones:
            row[x].append(y)
            col[y].append(x)

        count = 0
        start = stones[0]
        seen = set()

        for x,y in stones:
            if (x,y) in seen:
                continue
            count += 1
            seen = dfs((x,y), seen)
            
        return len(stones) - count