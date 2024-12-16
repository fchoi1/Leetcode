class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, n in enumerate(nums):
            heappush(heap, (n, i))

        for _ in range(k):
            val, i = heappop(heap)
            heappush(heap, (val * multiplier, i))

        heap.sort(key=lambda x: x[1])
        return [h[0] for h in heap]
        
        