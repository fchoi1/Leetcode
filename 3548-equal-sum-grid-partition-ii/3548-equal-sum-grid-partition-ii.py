from collections import defaultdict
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        H, W = len(grid), len(grid[0])

        # store positions of each value
        pos = defaultdict(list)
        for r in range(H):
            for c in range(W):
                pos[grid[r][c]].append((r, c))

        rows = [sum(row) for row in grid]
        cols = [sum(grid[r][c] for r in range(H)) for c in range(W)]
        total = sum(rows)

        def ok_remove(r, c, h, w, top, left):
            # rectangle connectivity rule
            if h > 1 and w > 1:
                return True
            if h == 1:
                return c == left or c == left + w - 1
            if w == 1:
                return r == top or r == top + h - 1
            return True

        def check(arr, horizontal):
            curr = 0
            for i, v in enumerate(arr[:-1]):
                curr += v
                other = total - curr
                if curr == other:
                    return True

                diff = abs(curr - other)
                if diff not in pos:
                    continue

                # determine larger section
                if curr > other:
                    # removing from first section
                    if horizontal:
                        h, w = i + 1, W
                        top, left = 0, 0
                        cells = [(r, c) for r, c in pos[diff] if r <= i]
                    else:
                        h, w = H, i + 1
                        top, left = 0, 0
                        cells = [(r, c) for r, c in pos[diff] if c <= i]
                else:
                    # removing from second section
                    if horizontal:
                        h, w = H - i - 1, W
                        top, left = i + 1, 0
                        cells = [(r, c) for r, c in pos[diff] if r > i]
                    else:
                        h, w = H, W - i - 1
                        top, left = 0, i + 1
                        cells = [(r, c) for r, c in pos[diff] if c > i]

                for r, c in cells:
                    if ok_remove(r, c, h, w, top, left):
                        return True

            return False

        return check(rows, True) or check(cols, False)