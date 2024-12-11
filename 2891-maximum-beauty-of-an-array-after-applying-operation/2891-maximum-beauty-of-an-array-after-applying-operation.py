class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        r = []
        for n in nums:
            r.append((n-k, n+k))
        r.sort()
        heap = []
        for s,e in r:
            if heap and s > heap[0]:
                heappop(heap)
            heappush(heap, e)
        return len(heap)
        