class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        n = len(grid)
        grid = [[c for c in row] for row in grid]
        graph = [[0] * (n * 3) for _ in range(n * 3)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    graph[i * 3][j * 3 + 2] = 1
                    graph[i * 3 + 1][j * 3 + 1] = 1
                    graph[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    graph[i * 3][j * 3] = 1
                    graph[i * 3 + 1][j * 3 + 1] = 1
                    graph[i * 3 + 2][j * 3 + 2] = 1

        def dfs(x, y):
            if 0 <= x < len(graph) and 0 <= y < len(graph) and graph[x][y] == 0:
                graph[x][y] = 1
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

        regions = 0
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] == 0:
                    dfs(i, j)
                    regions += 1

        return regions

    