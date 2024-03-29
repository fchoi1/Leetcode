class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        curr = heights[0]
        for i, h in enumerate(heights):
            diff = h - curr
            curr = h
            if diff > 0:
                if len(heap) < ladders:
                    heapq.heappush(heap, diff)
                elif len(heap) == ladders:
                    if ladders == 0 or diff < heap[0]:
                        bricks -= diff
                    else:
                        bricks -= heapq.heapreplace(heap, diff)
                    if bricks < 0:
                        return i - 1           
        return i
