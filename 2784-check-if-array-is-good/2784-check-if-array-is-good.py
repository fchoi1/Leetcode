class Solution:
    def isGood(self, nums: List[int]) -> bool:
        c = Counter(nums)
        N = len(nums) - 1
        return len(c) == N and c[N] == 2 and sum(nums) == N * (N + 1) // 2 + N