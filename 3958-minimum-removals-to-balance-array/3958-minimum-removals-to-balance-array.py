class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:

        l = 0
        N = len(nums)
        remove = N

        nums.sort()
        for i, n in enumerate(nums):
            while n > nums[l] * k:
                l += 1
            remove = min(remove, N - (i - l + 1))
        
        return remove
