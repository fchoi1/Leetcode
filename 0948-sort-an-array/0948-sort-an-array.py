class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for n in nums:
            heapq.heappush(heap,n)
        sorted_nums = []
        while heap:
            sorted_nums.append(heapq.heappop(heap))
        return sorted_nums
        