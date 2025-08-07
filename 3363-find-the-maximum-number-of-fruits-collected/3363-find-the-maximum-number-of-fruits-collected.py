class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:

        N = len(fruits)
        f = 0

        for i in range(N):
            f += fruits[i][i]

        downCache = defaultdict(int)
        rightCache = defaultdict(int)

        @lru_cache(None)
        def dfs(x, y, isDown):
            
           
            if isDown:
                direction = [(-1,1), (0,1), (1,1)]
            else:
                direction = [(1,-1), (1,0), (1,1)]

            total = 0
            for dx, dy in direction:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if isDown:
                        # determine area based on y for down
                        if (ny < N // 2 and nx >= N - 1 - ny) or (ny >= N //2 and nx > (N - 1 - (N - 1 - ny ))):
                            total = max(total, dfs(nx, ny, isDown))
                    else:
                        # determine if in area based on x for right
                        if (nx < N // 2 and ny >= N - 1 - nx) or (nx >= N //2 and ny > (N - 1 - (N - 1 - nx ))):
                            total = max(total, dfs(nx, ny, isDown))

            return total + fruits[y][x]

        down = dfs(N-1, 0, True)
        right = dfs(0, N-1, False)

        print(down, right)

        return f + down + right