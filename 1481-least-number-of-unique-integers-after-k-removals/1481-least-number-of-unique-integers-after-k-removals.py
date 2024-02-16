class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)

        heap = list(freq.values())
        heapq.heapify(heap)

        while k > 0 and heap:
            f = heap[0]
            if k >= f:
                k -= f
                heapq.heappop(heap)
            else:
                break

        return len(heap)