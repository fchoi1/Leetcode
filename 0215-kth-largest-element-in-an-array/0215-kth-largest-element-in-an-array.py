import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kHeap = []
        for n in nums:
            heapq.heappush(kHeap, n)
            if len(kHeap) > k:
                heapq.heappop(kHeap) 
        return  kHeap[0]
        