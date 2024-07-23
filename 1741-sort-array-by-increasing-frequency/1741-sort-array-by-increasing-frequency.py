class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        sorted_counts = sorted(counts.items(), key=lambda x: (x[1], -x[0]))
        ans = []
        for n, c in sorted_counts:
            ans.extend([n]*c)
        return ans