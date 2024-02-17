class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # use bricks for low elevation
        # use ladders for more

        # keep heap of ladders
        # use ladders on tallest gap
        # use bricks on lower gaps
        heap = []
        curr = heights[0]
        diffs = [0]
        for i, h in enumerate(heights):
            diff = h - curr
            if diff > 0:
                if len(heap) < ladders:
                    heapq.heappush(heap, diff)
                elif len(heap) == ladders:
                    if len(heap) == 0:
                        bricks -= diff
                    else:
                        if heap and diff < heap[0]:
                            minDiff = diff
                        else:
                            minDiff = heapq.heappop(heap)
                            heapq.heappush(heap, diff)
                        bricks -= minDiff
                    if bricks < 0:
                        return i - 1
                else:
                    return i - 1            
            curr = h
        print("done", i)
        return i
