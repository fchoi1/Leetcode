class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # =dijstras

        heap = [(0,0,0)] # time, x, y
        H = len(moveTime)
        W = len(moveTime[0])
        seen = set()
        while heap:
            currTime, x, y = heapq.heappop(heap)
            if (x,y) == (W-1, H-1):
                return currTime

            if (x,y) == (W-1, H-1):
                return currTime + 1

            if (x,y) in seen:
                continue
            seen.add((x,y))

            for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < W and 0 <= ny < H:
                    heapq.heappush(heap, ( max(currTime,moveTime[ny][nx]) + 1, nx, ny))
        
        return -1