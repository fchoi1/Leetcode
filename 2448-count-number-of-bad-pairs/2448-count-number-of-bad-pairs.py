class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        good = defaultdict(int)
        pairs = 0
        
        for i,n in enumerate(nums):
            diff = nums[i] - i
            good[diff] += 1
            pairs += good[diff]

        return N * (N + 1) // 2 - pairs
        