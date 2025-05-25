class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        return [n[0] for n in sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)[:k]]
        