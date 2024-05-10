class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = 0
        d = len(arr)-1

        for i in range(min(len(arr)-1, k)):
            heapq.heappush(heap, (arr[i]/arr[-1], i, len(arr)-1))

        for i in range(k):

            frac, n, d = heapq.heappop(heap)
            if d-1 > n:
                heapq.heappush(heap, (arr[n]/arr[d-1], n, d-1))

        return [arr[n], arr[d]]