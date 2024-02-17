class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        curr = heights[0]
        for i, h in enumerate(heights):
            diff = h - curr
            if diff > 0:
                if len(heap) < ladders:
                    heapq.heappush(heap, diff)
                elif len(heap) == ladders:
                    if len(heap) == 0 or diff < heap[0]:
                        bricks -= diff
                  
                    else:
                        bricks -= heapq.heappop(heap)
                        heapq.heappush(heap, diff)
                    if bricks < 0:
                        return i - 1           
            curr = h
        return i
