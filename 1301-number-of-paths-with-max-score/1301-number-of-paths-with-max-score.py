class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        W = len(board[0])
        H = len(board)
        mod = 10 ** 9 + 7

        NEG = -10**9
        dp = [[(NEG, 0) for _ in range(W)] for _ in range(H)]  # (score, ways)

        # Base case: E
        dp[H - 1][W - 1] = (0, 1)

        for y in range(H - 1, -1, -1):
            for x in range(W - 1, -1, -1):

                if board[y][x] == 'X':
                    continue

                if y == H - 1 and x == W - 1:
                    continue

                counts = 0
                curr = NEG

                # right
                if x + 1 < W:
                    score, ways = dp[y][x + 1]
                    if score > curr:
                        curr = score
                        counts = ways
                    elif score == curr:
                        counts = (counts + ways) % mod

                # down
                if y + 1 < H:
                    score, ways = dp[y + 1][x]
                    if score > curr:
                        curr = score
                        counts = ways
                    elif score == curr:
                        counts = (counts + ways) % mod

                # diagonal
                if y + 1 < H and x + 1 < W:
                    score, ways = dp[y + 1][x + 1]
                    if score > curr:
                        curr = score
                        counts = ways
                    elif score == curr:
                        counts = (counts + ways) % mod

                if counts == 0:
                    continue

                val = 0
                if board[y][x].isdigit():
                    val = int(board[y][x])

                dp[y][x] = (curr + val, counts)

        score, ways = dp[0][0]

        if ways == 0:
            return [0, 0]

        return [score % mod, ways % mod]