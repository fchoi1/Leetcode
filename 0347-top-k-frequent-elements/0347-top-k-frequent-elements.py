class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            counts = [(-v,k) for k,v in Counter(nums).items()] 
            heapify(counts)
            return [heappop(counts)[1] for _ in range(k)]