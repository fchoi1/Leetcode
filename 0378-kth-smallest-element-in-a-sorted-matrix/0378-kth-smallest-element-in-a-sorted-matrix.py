class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            for val in row:
                if len(heap) < k:
                    heapq.heappush(heap, -val)
                else:
                    if -heap[0] > val:
                        heapq.heapreplace(heap,-val)
        return -heap[0]
