class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        h = [(0,True,(0,0))] # time, step, (x,y)
        seen = set()
        W = len(moveTime[0])
        H = len(moveTime)

        while h:
     
            time, isEven, (x,y) = heapq.heappop(h)

            if (x,y) == (W-1,H-1):
                return time
            
            if (x,y) in seen:
                continue
            seen.add((x,y))

            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < W and 0 <= ny < H:
                    wait = 1 if isEven else 2
                    heapq.heappush(h, (max(time, moveTime[ny][nx]) + wait, not isEven, (nx, ny)))
        return -1