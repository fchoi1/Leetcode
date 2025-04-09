class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minVal = min(nums)
        if minVal < k:
            return -1
        unique = set(nums)
        return len(unique) - 1 if k in unique else len(unique)