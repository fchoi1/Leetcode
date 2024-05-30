class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_counts = sorted(counts.items(), reverse=True, key=lambda x: x[1])
        return [x[0] for x in sorted_counts[:k]]