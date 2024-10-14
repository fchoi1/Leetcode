class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # heap
        heap = []
        for n in nums:
            heappush(heap, -n)
        score = 0
        for i in range(k):
            curr = heappop(heap)
            score += -curr
            heappush(heap, -math.ceil(-curr/3))

        return score
        