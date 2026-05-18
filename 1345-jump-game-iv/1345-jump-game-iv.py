

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        pos = defaultdict(list)
        for i, val in enumerate(arr):
            pos[val].append(i)

        seen = set()


        h = [(0,0)] # steps, index

        while h:
            steps, idx = heappop(h)
            
            if idx < 0 or idx >= len(arr):
                continue

            if idx == len(arr) - 1:
                return steps

            if idx in seen:
                continue
            seen.add(idx)
            
            for nextIdx in pos[arr[idx]]:
                if nextIdx not in seen:
                    heappush(h, (steps + 1, nextIdx))
            pos[arr[idx]].clear()
            
            heappush(h, (steps + 1, idx - 1))
            heappush(h, (steps + 1, idx + 1))

        return -1