class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def get_positions(layer):
            top = layer
            left = layer
            bottom = m - layer - 1
            right = n - layer - 1

            pos = []

            # top
            for c in range(left, right + 1):
                pos.append((top, c))

            # right
            for r in range(top + 1, bottom):
                pos.append((r, right))

            # bottom
            for c in range(right, left - 1, -1):
                pos.append((bottom, c))

            # left
            for r in range(bottom - 1, top, -1):
                pos.append((r, left))

            return pos

        layers = min(m, n) // 2

        for layer in range(layers):

            pos = get_positions(layer)

            vals = [grid[r][c] for r, c in pos]

            rot = k % len(vals)
            vals = vals[rot:] + vals[:rot]

            for (r, c), val in zip(pos, vals):
                grid[r][c] = val

        return grid