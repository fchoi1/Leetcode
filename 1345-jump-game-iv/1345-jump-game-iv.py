from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:

        pos = defaultdict(list)

        for i, val in enumerate(arr):
            pos[val].append(i)

        q = deque([(0, 0)])  # idx, steps
        seen = {0}

        while q:
            idx, steps = q.popleft()

            if idx == len(arr) - 1:
                return steps

            # same value jumps
            for nextIdx in pos[arr[idx]]:
                if nextIdx not in seen:
                    seen.add(nextIdx)
                    q.append((nextIdx, steps + 1))

            # IMPORTANT FIX
            pos[arr[idx]].clear()

            # left
            if idx - 1 >= 0 and idx - 1 not in seen:
                seen.add(idx - 1)
                q.append((idx - 1, steps + 1))

            # right
            if idx + 1 < len(arr) and idx + 1 not in seen:
                seen.add(idx + 1)
                q.append((idx + 1, steps + 1))

        return -1